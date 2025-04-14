import cv2

# Inisialisasi kamera kiri dan kanan
cam_left = cv2.VideoCapture(0)  # Kamera kiri
cam_right = cv2.VideoCapture(1)  # Kamera kanan

# Loop utama untuk menangkap video dari kedua kamera
while True:
    # Membaca frame dari kamera kiri dan kanan
    retL, frameL = cam_left.read()
    retR, frameR = cam_right.read()

    # Periksa apakah frame berhasil ditangkap
    if not retL or not retR:
        print("Error capturing video")
        break

    # Tampilkan hasil kamera stereo
    cv2.imshow("Left Camera", frameL)
    cv2.imshow("Right Camera", frameR)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan resource kamera dan menutup semua jendela
cam_left.release()
cam_right.release()
cv2.destroyAllWindows()