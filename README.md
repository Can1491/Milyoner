# 🎮 Milyoner

Python ve Pygame kullanılarak geliştirilmiş, klasik bilgi yarışması formatından ilham alan grafik arayüzlü bir soru-cevap oyunu.

## 📌 Proje Hakkında

Oyuncu, farklı kategorilerden gelen soruları cevaplayarak para ağacında ilerlemeye çalışır.

Oyunda 3 can bulunur ve oyuncuya yardımcı olmak için iki farklı joker kullanılabilir:

- 50/50
- Seyirci

Oyuncu tüm soruları doğru cevaplayarak 1.000.000 TL ödüle ulaşabilir.

## 🎮 Özellikler

- 🎨 Pygame tabanlı grafik arayüz
- ❓ Soru-cevap sistemi
- 💰 500 TL'den 1.000.000 TL'ye kadar para ağacı
- ❤️ 3 can sistemi
- 5️⃣0️⃣/5️⃣0️⃣ jokeri
- 👥 Seyirci jokeri
- 🎲 Rastgele soru seçimi
- 🖱️ Fare ile kontrol
- 🏆 Kazanma ekranı
- 💀 Kaybetme ekranı
- 🔄 Yeniden başlatma sistemi
- ⏱️ Tıklama cooldown sistemi

## 🛠️ Kullanılan Teknolojiler

- Python
- Pygame

## 🎯 Oyun Mekanikleri

### 💰 Para Ağacı

Oyuncu doğru cevaplar verdikçe para ağacında ilerler.

En yüksek ödül:

**1.000.000 TL**

### ❤️ Can Sistemi

Oyuncunun toplam 3 hakkı bulunur.

Yanlış cevap verildiğinde bir hak kaybedilir.

Tüm haklar kaybedildiğinde oyun sona erer.

### 5️⃣0️⃣/5️⃣0️⃣ Jokeri

Bu joker kullanıldığında yanlış seçeneklerden ikisi kaldırılır ve oyuncunun karşısında iki seçenek bırakılır.

Joker oyun boyunca yalnızca bir kez kullanılabilir.

### 👥 Seyirci Jokeri

Seyirci jokeri, seçenekler için tahmini oy yüzdeleri oluşturur.

Doğru cevabın daha yüksek oy alma ihtimali bulunur.

Bu joker de oyun boyunca yalnızca bir kez kullanılabilir.

## ▶️ Kurulum

Öncelikle Python'un bilgisayarınızda kurulu olduğundan emin olun.

Pygame kütüphanesini yükleyin:

```bash
pip install pygame
