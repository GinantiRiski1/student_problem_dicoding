import streamlit as st
import pandas as pd
import joblib
import json
import numpy as np

# Load model dan fitur
model_data = joblib.load("model_rf.pkl")
model = model_data["model"]
selected_features = model_data["features"]

# Load mapping
with open("mapping.json", "r") as f:
    mappings = json.load(f)

# Fungsi bantu untuk mapping label ke angka
def map_input_to_numeric(feature, input_value):
    if feature in mappings:
        inv_map = {v: int(k) for k, v in mappings[feature].items()}
        return inv_map.get(input_value, 0)
    return input_value

st.set_page_config(page_title="🎓 Prediksi Status Mahasiswa", layout="wide")
st.title("🎓 Aplikasi Prediksi Status Mahasiswa")
st.markdown("Masukkan data mahasiswa untuk memprediksi apakah akan **Dropout**, **Masih Studi**, atau **Lulus**.")

st.markdown("### 🧾 Formulir Data Mahasiswa untuk Prediksi Kelulusan")

with st.form("student_form"):
    col1, col2, col3, col4, col5 = st.columns(5)
    input_data = {}

    # === KOLOM 1 ===
    with col1:
        st.markdown("#### 🎓 Pendidikan")
        input_data['Course'] = st.selectbox("📘 Program Studi", options=list(mappings['Course'].values()))
        input_data['Application_mode'] = st.selectbox("📝 Mode Aplikasi", options=list(mappings['Application_mode'].values()))
        input_data['Admission_grade'] = st.number_input("🧪 Nilai Penerimaan", min_value=0.0, max_value=200.0, value=150.0)
        input_data['Previous_qualification_grade'] = st.number_input("📄 Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=200.0, value=140.0)
        input_data['Age_at_enrollment'] = st.slider("🎂 Umur Saat Enroll", 17, 70, 25)

    # === KOLOM 2 ===
    with col2:
        st.markdown("#### 👪 Keluarga ")
        input_data['Fathers_occupation'] = st.selectbox("👨‍🔧 Pekerjaan Ayah", options=list(mappings['Fathers_occupation'].values()))
        input_data['Mothers_occupation'] = st.selectbox("👩‍🔧 Pekerjaan Ibu", options=list(mappings['Mothers_occupation'].values()))
        input_data['Fathers_qualification'] = st.selectbox("🎓 Kualifikasi Ayah", options=list(mappings['Fathers_qualification'].values()))
        input_data['Mothers_qualification'] = st.selectbox("🎓 Kualifikasi Ibu", options=list(mappings['Mothers_qualification'].values()))
        
        
    # === KOLOM 3 ===
    with col3:
        st.markdown("#### 📊 Sosial")
        input_data['GDP'] = st.number_input("💰 GDP", min_value=-5.00, max_value=5.00, value=0.0)
        input_data['Unemployment_rate'] = st.number_input("📉 Tingkat Pengangguran (%)", min_value=0.0, max_value=25.0, value=8.0)
        input_data['Inflation_rate'] = st.number_input("📈 Tingkat Inflasi (%)", min_value=-5.0, max_value=20.0, value=5.0)


    # === KOLOM 4 ===
    with col4:
        st.markdown("#### 🧮 Aktivitas Semester 1")
        input_data['Curricular_units_1st_sem_enrolled'] = st.slider("📚 Mata Kuliah 1st Sem", 0, 20, 5)
        input_data['Curricular_units_1st_sem_approved'] = st.slider("✅ Disetujui 1st Sem", 0, 20, 3)
        input_data['Curricular_units_1st_sem_grade'] = st.number_input("📏 Nilai Rata-rata 1st Sem", min_value=0.0, max_value=20.0, value=0.0)
        input_data['Curricular_units_1st_sem_evaluations'] = st.slider("🔍 Evaluasi 1st Sem", 0, 20, 4)
            
    with col5:
        st.markdown("#### 🧮 Aktivitas Semester 2")
        input_data['Curricular_units_2nd_sem_enrolled'] = st.slider("📚 Mata Kuliah 2nd Sem", 0, 20, 6)
        input_data['Curricular_units_2nd_sem_approved'] = st.slider("✅ Disetujui 2nd Sem", 0, 20, 4)
        input_data['Curricular_units_2nd_sem_grade'] = st.number_input("📏 Nilai Rata-rata 2nd Sem", min_value=0.0, max_value=20.0, value=0.0)
        input_data['Curricular_units_2nd_sem_evaluations'] = st.slider("🔍 Evaluasi 2nd Sem", 0, 20, 4)

    submit = st.form_submit_button("🎯 Prediksi Sekarang")



if submit:
    # Konversi input ke numerik berdasarkan mapping
    input_numeric = {
        feat: map_input_to_numeric(feat, val) for feat, val in input_data.items()
    }

    # Ambil semua fitur yang digunakan saat training
    all_features = model.feature_names_in_

    # Buat DataFrame kosong dengan semua fitur diisi 0
    full_input = pd.DataFrame(columns=all_features)
    full_input.loc[0] = 0

    # Isi nilai untuk fitur yang tersedia dari user input
    for feat in selected_features:
        if feat in input_numeric:
            full_input.at[0, feat] = input_numeric[feat]

    # Prediksi
    prediction = model.predict(full_input)[0]
    prob = model.predict_proba(full_input).max()

    # Mapping hasil prediksi
    status_map = {
    "Dropout": "❌ Dropout",
    "Enrolled": "⏳ Masih Studi",
    "Graduate": "✅ Lulus"
}

    st.markdown("---")
    st.subheader("📊 Hasil Prediksi:")
    st.success(f"🎓 **Status Mahasiswa:** `{status_map[prediction]}` (Probabilitas: `{prob:.2f}`)")
    # Tampilkan semua probabilitas kelas
    probas = model.predict_proba(full_input)[0]
    class_labels = model.classes_  # ['Dropout', 'Enrolled', 'Graduate']

    # Buat DataFrame untuk visualisasi
    proba_df = pd.DataFrame({
        "Status": class_labels,
        "Probabilitas": probas
    }).sort_values("Probabilitas", ascending=False)

    # Tampilkan tabel
    st.markdown("### 📊 Probabilitas Semua Kelas:")
    st.dataframe(proba_df.style.format({"Probabilitas": "{:.2%}"}), use_container_width=True)

    # Tampilkan grafik
    import altair as alt

    bar_chart = alt.Chart(proba_df).mark_bar().encode(
        x=alt.X('Probabilitas:Q', scale=alt.Scale(domain=[0, 1])),
        y=alt.Y('Status:N', sort='-x'),
        color=alt.Color('Status:N', legend=None),
        tooltip=['Status', alt.Tooltip('Probabilitas:Q', format='.2%')]
    ).properties(width=600, height=200)

    st.altair_chart(bar_chart)

