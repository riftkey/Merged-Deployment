import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK resources (may require additional installation steps)
nltk.download('punkt')

# Define pairs of patterns and responses (combine FAQ and Eliza-like)
pairs = [
    [
        r"(.*) (kesulitan|kendala|tidak bisa|gak bisa) (?:\s*(.*))? (membuka|mengunduh) (.*) (lampiran|resep|resep digital|catatan|surat|rekomendasi)",
        ["Maaf, kamu mengalami kendala membuka lampiran dokter. Coba perbarui aplikasi Halodoc ke versi terbaru. Jika masih ada kendala, hubungi CS kami untuk mendapatkan bantuan."]
    ],
    [
        r"^(.*)(cara|bisa) (mengirim|mengatur|melakukan|meminta) pengiriman instan(.*)$",
        ["""Jika kamu menggunakan pengiriman instan, kamu dapat menghubungi driver dengan cara berikut:\n
            Pilih ‘Riwayat’ dari menu Halodoc \n
            Pilih pesanan Toko Kesehatan yang sesuai \n
            Pilih pengiriman yang sesuai \n\n
            Temukan nama driver dan nomor ponsel dari atas layar pelacakan\n
         Catatan: Detail driver hanya akan muncul setelah driver ditugaskan untuk mengirimkan pesanan
        """,]
    ],
    [
        r"^(.*)(layanan|fitur)(.*) (ditawarkan|tersedia|halodoc)(.*)|Halodoc(.*) (menawarkan/layanan/fitur)(.*)",
        ["""
        Halodoc hadir dengan solusi kesehatan digital lengkap yang bisa diakses dari ponselmu, di mana saja, dan kapan saja.
        Layanan utama kami meliputi:

        1. Chat dengan Dokter: Chat dengan berbagai jenis dokter, spesialis dan ahli medis profesional secara langsung atau terjadwal. Kami juga punya dokter yang tersedia melalui panggilan suara atau video.
        2. Toko Kesehatan: Beli obat, produk kesehatan & alat medis, dan kirim ke tempatmu. Toko Kesehatan kami menjangkau pengiriman ke seluruh Indonesia, dan jika kamu butuh resep, kami bisa sambungkan kamu dengan dokter untuk meminta resepnya.
        3. Home Lab & Vaksinasi: Lakukan tindakan tes lab, vaksinasi, atau vitamin booster dari rumah atau di lokasi yang dipilih. Kamu bisa pilih tindakan yang sesuai kebutuhanmu dan dapatkan saran medis pasca tindakan dari mitra dokter kami.

        Jelajahi juga layanan kami lainnya. Cukup pilih ‘Lihat Semua’ pada menu layanan dari beranda Halodoc kamu.
        """,]
    ],
    [
        r"(.*)(melakukan|lakukan)(.*)(konsultasi|konsultasi online)(.*)",
        ["""
        Chat dengan Dokter menyediakan layanan konsultasi online dengan berbagai dokter, spesialis, dan tenaga medis tepercaya. Kamu bisa konsultasi melalui chat, panggilan audio, dan panggilan video. Jika asuransimu disambungkan ke Halodoc, konsultasimu juga bisa ditanggung.
        Di Chat dengan Dokter, kamu bisa langsung chat dengan dokter yang tersedia, ditandai dengan titik hijau. Selain itu, kamu juga bisa menjadwalkan konsultasi sesuai dengan kebutuhanmu. Dari konsultasi tersebut, kamu bisa dapatkan saran medis, resep obat, rekomendasi istirahat, dan dokumen lain yang dapat membantumu menangani kondisi kesehatanmu.
        Mohon diingat bahwa Halodoc tidak ditujukan untuk situasi gawat darurat. Jika kamu dalam keadaan gawat darurat, segera hubungi nomor layanan medis darurat (Call Center 112) atau kunjungi fasilitas kesehatan terdekat.

        Ikuti langkah berikut untuk berkonsultasi online di Halodoc:
        1. Pilih 'Chat dengan Dokter' pada halaman utama aplikasi Halodoc.
        2. Cari dokter yang sesuai dengan kebutuhanmu. Kamu dapat pilih berdasarkan spesialisasi, atau mencari berdasarkan nama dokter, spesialisasi, atau gejala.
        3. Pilih 'Konsultasi Sekarang' untuk mulai konsultasi segera.
        4. Pilih profil pasien yang perlu penanganan. Jika kamu berkonsultasi mewakili orang lain, pilih profil orang tersebut.
        5. Selesaikan pembayaranmu.
        6. Konsultasimu akan dimulai setelah kamu menyelesaikan pembayaran dan dokter menerima permintaanmu.
        """,]
    ],
    [
        r"(bagaimana|saya)(.*)(belum tahu|tidak tahu)(.*)(konsultasi|berkonsultasi|obat|obatnya)(.*)(spesialis|dokter|obat|mana|apa)",
        ["""
        Jika kamu sakit atau butuh bantuan konsultasi, namun belum tahu perlu konsultasi ke spesialis apa atau beli obat apa, konsultasi dengan mitra dokter umum Halodoc terlebih dahulu.

        Dokter umum kami dapat merujuk kamu ke spesialis online yang sesuai atau memberikanmu resep obat yang kamu butuhkan. Lihat cara untuk konsultasi di FAQ ini: Bagaimana cara konsultasi online di Halodoc?

        Setelah konsultasi dengan dokter dan mendapat resep, kamu bisa ke Toko Kesehatan untuk menebus obat yang kamu butuhkan. Lihat caranya di FAQ ini: Bagaimana cara menebus resep di Halodoc?

        Kamu juga bisa mencari obat berdasarkan gejala yang kamu alami. Berikut caranya:
        1. Pilih 'Toko Kesehatan' pada halaman utama Halodoc.
        2. Pada kolom pencarian, ketik gejala yang kamu alami.
        3. Obat-obatan yang mungkin kamu butuhkan akan muncul di hasil pencarian
        """,]
    ],
    [
        r"(tolong|jelasin|tutorial|bisa|bagaimana|gimana|saya)(.*)(beli)(.*)(obat)(.*)",
        ["""
        Berikut cara membeli obat di Halodoc:
        1. Pada halaman utama Halodoc, pilih “Toko Kesehatan”
        2. Pilih kategori yang kamu inginkan atau klik “Lihat Semua Kategori”, lalu pilih obat yang kamu inginkan
        3. Kamu juga bisa menggunakan kolom pencarian untuk mengetikkan nama obat yang kamu cari
        """,]
    ],
    [
        r"(apakah|halodoc|ada|saya)(.*)(konsultasi|layanan|layanan kesehatan)(.*)(offline|luring|di tempat|langsung)",
        ["""
        Halodoc menyediakan Home Lab & Vaksinasi, layanan untuk mendapatkan tindakan tes lab, vaksinasi, atau vitamin booster dari rumah atau di lokasi mana pun yang kamu pilih.
        Tindakan ini akan dilaksanakan oleh staf medis, perawat, atau dokter yang tersertifikasi.
        Dengan Home Lab & Vaksinasi, kamu dapat menikmati pengalaman yang serba digital! Cari dan temukan tindakan yang sesuai dengan kebutuhanmu dari katalog kami, lalu bayar menggunakan metode pilihanmu. Staf medis kami akan tiba di lokasimu pada slot waktu yang kamu pilih untuk melakukan tindakan.
        Jika kamu memesan tes lab, kamu akan mendapatkan notifikasi saat hasilmu sudah tersedia, dan kamu dapat melihat hasilnya di aplikasi Halodoc. Kamu juga akan mendapatkan kupon untuk konsultasi online setelah pesananmu selesai, sehingga kamu dapat konsultasi dengan dokter kami jika kamu butuh bantuan memahami hasil tesmu.
        """,]
    ],
    [
        r"(Bagaimana|gimana|saya|halodoc|apakah)(.*)(mesan|pesan|reservasi)(.*)(home lab|vaksin)",
        ["""
          Ikuti langkah berikut untuk memesan tindakan dari Home Lab & Vaksinasi:
          1. Pilih 'Home Lab & Vaksinasi' pada halaman utama aplikasi Halodoc.
          2. Cari tindakan yang kamu perlukan dan tambahkan ke keranjangmu.
          3. Setelah menambahkan semua tindakan yang kamu butuhkan ke keranjang, pilih 'Lihat Keranjang'.
          4. Pilih pasien yang akan mendapatkan tindakan serta alamat tindakan.
          5. Pastikan kamu telah memilih semua tindakan yang dibutuhkan, lalu pilih 'Jadwalkan'.
          6. Jika profil yang dipilih belum terverifikasi, kamu perlu memverifikasinya sebelum melanjutkan pemesanan.
          7. Pilih slot waktu tindakan. Slot ini adalah waktu staf medis kami akan tiba di alamat yang kamu pilih. Setelah memilih slot, pilih 'Pesan'.
          8. Pilih metode pembayaran, kemudian pilih 'Bayar & Konfirmasi'.
          9. Pesanan kamu berhasil dibuat. Kamu dapat melihat detail pesanan, menghubungi staf medis, atau melacak progres sampel dan hasil tes yang dipesan di 'Riwayat Transaksi'.
        """,]
    ],
    [
        r"(bisa|saya|gimana|bagaimana|apakah)(.*)(pesan|mesan|mesen|reservasi)(.*)(tes lab|test lab |tes satuan|test)",
        ["""
        Ikuti langkah berikut untuk memesan tes lab satuan dari Home Lab & Vaksinasi:
        1. Pilih 'Home Lab & Vaksinasi' pada halaman utama aplikasi Halodoc.
        2. Pilih 'Tes Lab Satuan' pada bagian 'Cari Berdasarkan Jenis Layanan'.
        3. Kamu bisa mencari dan menambahkan tes lab satuan ke keranjangmu dari sini.
        """,]
    ],
    [
        r"(.*)(pesen|pesan|mesan|mesen|reservasi)(.*)(konsultasi online|konsultasi)(.*)(teman|orang lain|keluarga|papa|mama|kakak|adik|om|tante|selain saya|nenek|kakek|teman|pacar|suami|istri|ibu|ayah|bapak)",
        ["""
        Ya, jika keluarga atau temanmu sakit, kamu dapat berkonsultasi secara online untuk mereka.
        Saat memesan konsultasi, pastikan kamu memilih pasien yang ditujukan dengan benar agar pasien mendapatkan resep obat yang tepat atau dapat menggunakan manfaat asuransi.

        Ikuti langkah berikut untuk memesan konsultasi untuk orang lain:
        1. Pilih 'Chat Dengan Dokter'.
        2. Cari dokter yang ingin kamu konsultasikan dan pilih 'Chat'.
        3. Pilih anggota keluarga yang ingin berkonsultasi. Jika anggota keluarga belum terdaftar, pilh 'Profil Baru' pada pojok kanan atas halaman.
        4. Lanjutkan pembayaran.
        """,]
    ],
    [
        r"(.*)(jadwal)(.*)(konsultasi online|konsultasi)",
        ["""
        Ikuti langkah berikut untuk menjadwalkan konsultasi online:
        1. Pilih 'Chat dengan Dokter' pada menu bagian bawah layar.
        2. Cari dan pilih dokter sesuai dengan kebutuhanmu.
        3. Jika dokter mengizinkan konsultasi terjadwal, profil dokter akan memiliki tombol 'Jadwalkan', atau kamu mendapatkan pilihan untuk 'Konsultasi Nanti' setelah kamu pilih 'Chat'.
        4. Pilih tanggal dan waktu konsultasi.
        5. Pilih profil pasien. Jika pasien belum mempunyai profil di Halodoc, pilih 'Profil Baru' pada bagian kanan atas layar, dan buat profil baru.
        6. Lanjutkan ke halaman pembayaran.
        7. Jadwal konsultasi berhasil dibuat.

        Kamu akan mendapatkan notifikasi sebelum konsultasi dimulai. Mohon diperhatikan bahwa kami hanya mempunyai waktu tunggu 10 menit untuk janji konsultasi. Jika kamu tidak bergabung dalam waktu tersebut, konsultasimu akan ditandai sebagai selesai.

        """,]
    ],
    [
        r"(.*)darurat",
        ["""Segera hubungi bantuan medis darurat (Call Center 112) atau kunjungi fasilitas kesehatan terdekatmu. Pastikan untuk memberikan informasi penting seperti gejala yang dialami, alamat rumah, nomor ponsel, dan riwayat medis jika ada.
        Mohon dipahami bahwa Halodoc tidak digunakan sebagai penanganan untuk kondisi darurat.
        """,]
    ],
    [
        r"(.*)",
        ["""Mohon maaf, bolehkah anda mengulangi pertanyaan anda?
        """,]
    ],
]

# Define reflection pairs (optional for basic mirroring)
reflections = reflections

# Create the chatbot object
chatbot = Chat(pairs, reflections)
