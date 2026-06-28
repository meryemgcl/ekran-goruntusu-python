# 📸 Python Otomatik Ekran Görüntüsü Alma Aracı

Bu proje, Python kullanarak belirlenen zaman damgası (timestamp) formatıyla otomatik olarak ekran görüntüsü alan ve seçilen bir klasöre kaydeden basit, kararlı ve etkili bir betiktir.

## 🚀 Özellikler

* **Zaman Damgalı İsimlendirme:** Her ekran görüntüsü `screenshot_YYYY-MM-DD_HH-MM-SS.png` formatıyla kaydedilir, böylece dosyalar birbirinin üzerine yazılmaz.
* **Özel Klasör Desteği:** Ekran görüntülerinin bilgisayarınızda tam olarak nereye kaydedileceğini dinamik olarak belirleyebilirsiniz.

## 🛠️ Gereksinimler ve Kurulum

Projenin çalışabilmesi için sisteminizde Python 3 ve gerekli kütüphanelerin yüklü olması gerekir.

1. **Bağımlılıkları Yükleyin:**
   ```bash
   pip install pyautogui Pillow pyscreeze
