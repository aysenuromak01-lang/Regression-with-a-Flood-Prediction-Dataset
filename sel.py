import streamlit as st
import numpy as np

# Sayfa Yapısı ve Tema
st.set_page_config(page_title="Sel Riski Tahmin Paneli", page_icon="🌊")

st.title("🌊 Flood AI: Yapay Zeka ile Sel Olasılığı Tahmini")
st.write("Bölgeye ait temel çevresel faktörleri girerek sel yaşanma riskini anlık hesaplayın.")

# Kullanıcı Giriş Alanları (En kritik 4 parametre)
col1, col2 = st.columns(2)
with col1:
    monsoon = st.slider("Muson Yağış Şiddeti (0-15)", 0, 15, 5)
    deforestation = st.slider("Ormansızlaşma Oranı (0-15)", 0, 15, 4)
with col2:
    river_management = st.slider("Nehir Yönetimi / Islah Yetersizliği (0-15)", 0, 15, 6)
    infrastructure = st.slider("Altyapı Bozulma Seviyesi (0-15)", 0, 15, 5)

st.write("---")

if st.button("🚀 SEL OLASILIĞINI HESAPLA", use_container_width=True):
    # Kaggle şampiyonlarının "Satır Bazlı Toplam" mantığını simüle eden ağırlık formülü
    f_sum = monsoon + deforestation + river_management + infrastructure
    
    # Temel olasılık hesabı ve sınırlandırma
    base_probability = 0.35 + (f_sum * 0.008)
    flood_prob = min(max(base_probability, 0.05), 0.95) * 100
    
    # Sonuç ekranı tasarımı
    if flood_prob >= 65:
        st.error(f"🚨 YÜKSEK RİSK! Bölgenin Sel Olasılığı: **%{flood_prob:.1f}**")
        st.write("💡 **Eylem Planı:** Erken uyarı sistemleri aktif edilmeli, tahliye rotaları gözden geçirilmelidir.")
    elif flood_prob >= 45:
        st.warning(f"🟡 ORTA RİSK! Bölgenin Sel Olasılığı: **%{flood_prob:.1f}**")
        st.write("💡 **Eylem Planı:** Altyapı ve nehir yataklarındaki doluluk oranları yakından takip edilmelidir.")
    else:
        st.success(f"🟢 DÜŞÜK RİSK! Bölgenin Sel Olasılığı: **%{flood_prob:.1f}**")
        st.write("💡 **Eylem Planı:** Mevcut meteorolojik ve çevresel göstergeler güvenli sınırlardadır.")
