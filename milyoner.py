import pygame
import random
import time

pygame.init()

# Ekran Ayarları
WIDTH, HEIGHT = 1200, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MİLYONER")

# Fontlar
font = pygame.font.SysFont("Segoe UI", 20, bold=True)
big_font = pygame.font.SysFont("Segoe UI", 45, bold=True)
title_font = pygame.font.SysFont("Segoe UI", 70, bold=True)

# ---------------- Sorular ----------------
all_questions = [
    ("Türkiye'nin başkenti neresidir?", ["A) İstanbul", "B) Ankara", "C) İzmir", "D) Bursa"], 1),
    ("Python adını nereden almıştır?", ["A) Yılan türü", "B) Monty Python", "C) Antik şehir", "D) Geliştirici"], 1),
    ("Bir byte kaç bitten oluşur?", ["A) 4", "B) 8", "C) 16", "D) 32"], 1),
    ("Dünya'nın en yüksek dağı hangisidir?", ["A) Everest", "B) K2", "C) Erciyes", "D) Fuji"], 0),
    ("Güneş sistemindeki en büyük gezegen?", ["A) Mars", "B) Jüpiter", "C) Satürn", "D) Venüs"], 1),
    ("İstiklal Marşı'nın yazarı kimdir?", ["A) Ziya Gökalp", "B) M. Akif Ersoy", "C) Reşat Nuri", "D) Namık Kemal"], 1),
    ("Hangisi bir programlama dili değildir?", ["A) Java", "B) C++", "C) HTML", "D) Python"], 2),
    ("Fatih Sultan Mehmet kaç yılında İstanbul'u fethetti?", ["A) 1071", "B) 1299", "C) 1453", "D) 1517"], 2),
    ("Kimya sembolü 'Au' olan element hangisidir?", ["A) Gümüş", "B) Bakır", "C) Altın", "D) Demir"], 2),
    ("Hangi gezegen 'Kızıl Gezegen' olarak bilinir?", ["A) Venüs", "B) Mars", "C) Neptün", "D) Merkür"], 1),
    ("Türk lirasından 6 sıfır kaç yılında atılmıştır?", ["A) 2000", "B) 2005", "C) 2010", "D) 2012"], 1),
    ("Türkiye'nin en büyük gölü hangisidir?", ["A) Tuz Gölü", "B) Van Gölü", "C) Beyşehir Gölü", "D) İznik Gölü"], 1),
    ("Telefonu kim icat etmiştir?", ["A) Newton", "B) Graham Bell", "C) Edison", "D) Tesla"], 1),
    ("Pusula hangi yönü gösterir?", ["A) Doğu", "B) Batı", "C) Kuzey", "D) Güney"], 2),
    ("Galatasaray hangi yıl UEFA kupasını almıştır?", ["A) 1998", "B) 2000", "C) 2002", "D) 2004"], 1),
    ("Türkiye'nin yüzölçümü en büyük ili hangisidir?", ["A) Ankara", "B) Konya", "C) Erzurum", "D) Sivas"], 1),
    ("Yerçekimini kim keşfetmiştir?", ["A) Einstein", "B) Tesla", "C) Newton", "D) Galileo"], 2),
    ("Mona Lisa tablosu kime aittir?", ["A) Van Gogh", "B) Picasso", "C) Da Vinci", "D) Dali"], 2),
    ("Yedi tepeli şehir olarak bilinen ilimiz?", ["A) Bursa", "B) İzmir", "C) İstanbul", "D) Ankara"], 2),
    ("İlk Türk devletlerinde hükümdara verilen ünvan?", ["A) Sultan", "B) Şah", "C) Han", "D) Padişah"], 2),
    ("Sıfırı bulan matematikçi kimdir?", ["A) Harezmi", "B) Ömer Hayyam", "C) Pisagor", "D) Arşimet"], 0),
    ("Türkiye'nin en kuzey noktası?",
     ["A) Sinop İnceburun", "B) Hatay Beysun", "C) Edirne Kapıkule", "D) Iğdır Dilucu"], 0),
    ("Atatürk kaç yılında doğmuştur?", ["A) 1876", "B) 1881", "C) 1885", "D) 1938"], 1),
    ("Hangisi bir işletim sistemidir?", ["A) Google", "B) Windows", "C) Facebook", "D) Amazon"], 1),
    ("Bir gün kaç saniyedir?", ["A) 3600", "B) 43200", "C) 86400", "D) 100000"], 2),
    ("Satrancın başlangıcında her oyuncunun kaç taşı vardır?", ["A) 12", "B) 16", "C) 20", "D) 32"], 1),
    ("En uzun ömürlü hayvan hangisidir?", ["A) Fil", "B) Dev Kaplumbağa", "C) Balina", "D) Timsah"], 1),
    ("Oksijenin atom numarası kaçtır?", ["A) 6", "B) 8", "C) 12", "D) 16"], 1),
    ("Hangisi asal sayıdır?", ["A) 1", "B) 9", "C) 2", "D) 15"], 2),
    ("İlk internet bağlantısı hangi ülkede yapılmıştır?", ["A) Rusya", "B) Çin", "C) ABD", "D) Almanya"], 2),
    ("Dünya'nın katmanlarından hangisi en dıştadır?", ["A) Mantol", "B) Çekirdek", "C) Yer kabuğu", "D) Magma"], 2),
    ("Avustralya'nın başkenti neresidir?", ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth"], 2),
    ("Gözdeki renkli kısma ne denir?", ["A) Pupil", "B) İris", "C) Retira", "D) Kornea"], 1),
    ("İnce Memed kimin eseridir?", ["A) Orhan Pamuk", "B) Yaşar Kemal", "C) Elif Şafak", "D) Sabahattin Ali"], 1),
    ("Kıbrıs Barış Harekatı hangi yıldır?", ["A) 1963", "B) 1974", "C) 1980", "D) 1991"], 1),
    ("Kaç tane ana yön vardır?", ["A) 2", "B) 4", "C) 6", "D) 8"], 1),
    ("Işık hızı saniyede yaklaşık kaç km'dir?", ["A) 100.000", "B) 300.000", "C) 500.000", "D) 1.000.000"], 1),
    ("En sert maden hangisidir?", ["A) Demir", "B) Elmas", "C) Çelik", "D) Kuvars"], 1),
    ("Hangi organımız kanı pompalar?", ["A) Karaciğer", "B) Akciğer", "C) Kalp", "D) Mide"], 2),
    ("Pi sayısının ilk üç basamağı?", ["A) 3.12", "B) 3.14", "C) 3.16", "D) 3.18"], 1),
    ("Amazon Nehri hangi kıtadadır?", ["A) Afrika", "B) Güney Amerika", "C) Asya", "D) Avrupa"], 1),
    ("Kanuni Sultan Süleyman kaç yıl tahtta kaldı?", ["A) 36", "B) 40", "C) 46", "D) 50"], 2),
    ("Hangi ülkenin bayrağında akçaağaç yaprağı vardır?", ["A) ABD", "B) Kanada", "C) Avustralya", "D) İsveç"], 1),
    ("Mıknatıs hangi metali çekmez?", ["A) Demir", "B) Nikel", "C) Kobalt", "D) Bakır"], 3),
    ("İlk Türk kadın pilot kimdir?", ["A) Sabiha Gökçen", "B) Leyla Gencer", "C) Halide Edip", "D) Afife Jale"], 0),
    ("Nobel ödülleri hangi ülkede verilir?", ["A) Almanya", "B) İsveç", "C) Fransa", "D) İngiltere"], 1),
    ("Everest Dağı hangi iki ülke sınırındadır?",
     ["A) Hindistan-Çin", "B) Nepal-Çin", "C) Pakistan-Hindistan", "D) Butan-Nepal"], 1),
    ("Hangi nota daha kalındır?", ["A) Do", "B) Re", "C) Mi", "D) Fa"], 0),
    ("Mimar Sinan'ın 'Ustalık Eserim' dediği cami?", ["A) Süleymaniye", "B) Selimiye", "C) Şehzade", "D) Sultanahmet"],
     1),
    ("İnsan vücudundaki en sert yapı hangisidir?", ["A) Kafatası", "B) Uyluk Kemiği", "C) Diş Minesi", "D) Omurga"], 2),
]
#Para ağacı
money_tree = ["500 TL", "1.000 TL", "5.000 TL", "10.000 TL", "20.000 TL", "40.000 TL", "60.000 TL", "125.000 TL",
              "250.000 TL", "500.000 TL", "1.000.000 TL"]

# ---------------- STATE ----------------
level = 0
lives = 3
game_won = False
current_index = 0
deck = []

joker_5050_used = False
joker_5050_active = False
joker_audience_used = False
joker_audience_active = False
fifty_cache = [0, 1, 2, 3]
audience_target = [0, 0, 0, 0]
audience_current = [0, 0, 0, 0]

lock = False
lock_time = 0
COOLDOWN = 0.5


def reset():
    global level, lives, deck, current_index, game_won, joker_5050_used, joker_5050_active
    global joker_audience_used, joker_audience_active, fifty_cache, audience_target, audience_current
    level = 0
    lives = 3
    game_won = False
    joker_5050_used = False
    joker_5050_active = False
    joker_audience_used = False
    joker_audience_active = False
    fifty_cache = [0, 1, 2, 3]
    audience_current = [0, 0, 0, 0]
    # Karıştırılmış yeni bir deste oluştur
    deck = random.sample(range(len(all_questions)), len(all_questions))
    current_index = deck.pop()


def next_question():
    global level, game_won, joker_5050_active, joker_audience_active, fifty_cache
    joker_5050_active = False
    joker_audience_active = False
    fifty_cache = [0, 1, 2, 3]

    # 11. soru bildiğinde (indeks 10'dan sonra) oyunu bitir
    if level >= len(money_tree):
        game_won = True
        return -1

    return deck.pop() if len(deck) > 0 else -1


def button(text, x, y, w, h, mouse, base_color=(40, 40, 60), hover_color=(90, 160, 255)):
    r = pygame.Rect(x, y, w, h)
    color = hover_color if r.collidepoint(mouse) else base_color
    pygame.draw.rect(screen, color, r, border_radius=15)
    pygame.draw.rect(screen, (255, 255, 255), r, 2, border_radius=15)
    txt = font.render(text, True, (255, 255, 255))
    screen.blit(txt, txt.get_rect(center=r.center))
    return r


def draw_end_screen(title, subtitle, bg_color, accent_color):
    screen.fill(bg_color)
    pygame.draw.circle(screen, accent_color, (600, 325), 400, 5)
    pygame.draw.circle(screen, accent_color, (600, 325), 300, 2)
    title_surf = title_font.render(title, True, (255, 255, 255))
    sub_surf = big_font.render(subtitle, True, (220, 220, 220))
    screen.blit(title_surf, title_surf.get_rect(center=(600, 220)))
    screen.blit(sub_surf, sub_surf.get_rect(center=(600, 320)))
    btn_color = (accent_color[0] // 2, accent_color[1] // 2, accent_color[2] // 2)
    return button("YENİDEN BAŞLAT", 450, 450, 300, 65, pygame.mouse.get_pos(), btn_color, accent_color)


reset()

# ---------------- OYUN DÖNGÜSÜ ----------------
running = True
while running:
    screen.fill((15, 15, 35))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    if lock and time.time() - lock_time > COOLDOWN: lock = False

    # KAZANMA EKRANI
    if game_won:
        btn = draw_end_screen("TEBRİKLER!", "MİLYONER OLDUNUZ!", (10, 40, 10), (0, 200, 100))
        if btn.collidepoint(mouse) and click[0] and not lock:
            lock = True;
            lock_time = time.time()
            reset()
        pygame.display.update();
        continue

    # KAYBETME EKRANI
    if lives <= 0:
        won_money = money_tree[level - 1] if level > 0 else "0 TL"
        btn = draw_end_screen("OYUN BİTTİ", f"Kazancınız: {won_money}", (40, 10, 10), (200, 0, 0))
        if btn.collidepoint(mouse) and click[0] and not lock:
            lock = True;
            lock_time = time.time()
            reset()
        pygame.display.update();
        continue

    # Soru çekme (Deste biterse oyunu bitir)
    if current_index == -1:
        game_won = True
        continue

    q, opts, answer = all_questions[current_index]

    # ---------------- PARA AĞACI ----------------
    tree_x, tree_y, tree_w = 940, 40, 240
    pygame.draw.rect(screen, (25, 25, 50), (tree_x, tree_y, tree_w, 580), border_radius=15)
    pygame.draw.rect(screen, (100, 100, 255), (tree_x, tree_y, tree_w, 580), 2, border_radius=15)

    for i, m in enumerate(money_tree[::-1]):
        idx = len(money_tree) - 1 - i
        color = (255, 255, 255)
        prefix_color = (255, 150, 0) if idx in [0, 5, 10] else (100, 100, 255)

        if idx == level:
            pygame.draw.rect(screen, (70, 70, 150), (tree_x + 5, 65 + i * 50, tree_w - 10, 40), border_radius=8)
            color = (255, 255, 0)
        elif idx < level:
            color = (100, 100, 120)

        pygame.draw.circle(screen, prefix_color, (tree_x + 35, 87 + i * 50), 3)
        txt = font.render(m, True, color)
        screen.blit(txt, (tree_x + 55, 72 + i * 50))

    # ---------------- SORU VE JOKERLER ----------------
    pygame.draw.rect(screen, (30, 30, 70), (250, 60, 650, 120), border_radius=20)
    pygame.draw.rect(screen, (100, 100, 255), (250, 60, 650, 120), 3, border_radius=20)
    q_surf = font.render(q, True, (255, 255, 255))
    screen.blit(q_surf, q_surf.get_rect(center=(575, 120)))

    f50_btn = button("50/50", 40, 60, 160, 55, mouse, (100, 30, 30) if joker_5050_used else (40, 40, 80))
    aud_btn = button("SEYİRCİ", 40, 125, 160, 55, mouse, (100, 30, 30) if joker_audience_used else (40, 40, 80))

    if f50_btn.collidepoint(mouse) and click[0] and not joker_5050_used and not lock:
        wrong_opts = [i for i in range(4) if i != answer]
        fifty_cache = [answer, random.choice(wrong_opts)]
        joker_5050_used = True;
        joker_5050_active = True
        lock = True;
        lock_time = time.time()

    if aud_btn.collidepoint(mouse) and click[0] and not joker_audience_used and not lock:
        votes = [random.randint(5, 15) for _ in range(4)]
        votes[answer] += random.randint(50, 70)
        total = sum(votes)
        audience_target = [int(v * 100 / total) for v in votes]
        joker_audience_used = True;
        joker_audience_active = True
        lock = True;
        lock_time = time.time()

    if joker_audience_active:
        px, py = 40, 200
        pygame.draw.rect(screen, (20, 20, 40), (px, py, 180, 200), border_radius=15)
        pygame.draw.rect(screen, (100, 100, 200), (px, py, 180, 200), 2, border_radius=15)
        for i in range(4):
            audience_current[i] += (audience_target[i] - audience_current[i]) * 0.08
            val = audience_current[i]
            x_bar = px + 25 + i * 38
            bar_height = int(val * 1.3)
            pygame.draw.rect(screen, (40, 40, 60), (x_bar, py + 160 - 130, 20, 130))
            pygame.draw.rect(screen, (0, 255, 150), (x_bar, py + 160 - bar_height, 20, bar_height))
            screen.blit(font.render("ABCD"[i], True, (255, 255, 255)), (x_bar + 2, py + 165))
            percent_txt = font.render(f"{int(val)}", True, (0, 255, 150))
            screen.blit(percent_txt, (x_bar - 5, py + 160 - bar_height - 25))

    # ---------------- SEÇENEKLER ----------------
    for i in range(4):
        if joker_5050_active and i not in fifty_cache: continue
        bx, by = 300, 240 + (i * 85)
        b = button(opts[i], bx, by, 550, 65, mouse)
        if b.collidepoint(mouse) and click[0] and not lock:
            lock = True;
            lock_time = time.time()
            if i == answer:
                level += 1
                current_index = next_question()
            else:
                lives -= 1
                current_index = next_question()

    # ---------------- CANLAR VE METİN ----------------
    life_text = font.render("KALAN HAK:", True, (255, 255, 255))
    screen.blit(life_text, (30, 20))
    for i in range(3):
        color = (255, 50, 50) if i < lives else (50, 50, 50)
        pygame.draw.circle(screen, color, (170 + i * 30, 35), 10)

    pygame.display.update()

pygame.quit()