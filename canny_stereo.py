import cv2
import numpy as np

def canny_edge_detection(image):
    """
    Fungsi untuk mendeteksi tepi menggunakan Canny Edge Detection.
    """
    # Konversi gambar ke grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Menghaluskan gambar menggunakan Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Deteksi tepi menggunakan Canny
    edges = cv2.Canny(blur, 50, 150)
    return edges

# Inisialisasi kamera stereo
cam_left = cv2.VideoCapture(0)  # Kamera kiri
cam_right = cv2.VideoCapture(1)  # Kamera kanan

# Loop utama untuk menangkap dan memproses video
while True:
    # Membaca frame dari kamera kiri dan kanan
    retL, frameL = cam_left.read()
    retR, frameR = cam_right.read()

    # Periksa apakah frame berhasil ditangkap
    if not retL or not retR:
        print("Error capturing video")
        break

    # Proses Canny Edge Detection
    edgesL = canny_edge_detection(frameL)
    edgesR = canny_edge_detection(frameR)

    # Tampilkan hasil deteksi tepi
    cv2.imshow("Canny Left", edgesL)
    cv2.imshow("Canny Right", edgesR)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Melepaskan resource kamera dan menutup semua jendela
cam_left.release()
cam_right.release()
cv2.destroyAllWindows()