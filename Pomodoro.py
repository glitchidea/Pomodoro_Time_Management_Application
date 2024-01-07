import time
import os

def main():
    minutes = 25 # pomodoro süresi
    sets = 4 # pomodoro set sayısı
    break_time = 5 # mola süresi
    sound_file = r'C:\Windows\Media\Alarm09.wav' # kullanılacak ses dosyası

    tasks = []
    while True:
        os.system('cls')
        print(f"Pomodoro Süresi: {minutes} dakika\nPomodoro Set Sayısı: {sets}\n")
        print("Yapılacaklar Listesi:\n")
        for index, task in enumerate(tasks):
            if task["done"]:
                print(f"{index + 1}. [X] {task['name']}")
            else:
                print(f"{index + 1}. [ ] {task['name']}")
        print("\n")

        choice = input("Yapmak istediğiniz işlemi seçin:\n1. Yeni görev ekle\n2. Görev tamamlandı\n3. Görev sil\n4. Pomodoro'ya başla\n5. Ayarlar\n6. Çıkış\n")

        if choice == "1":
            while True:
                os.system('cls')
                print("Pomodoro devam ediyor, yeni bir görev ekleyebilirsiniz. Görev eklemeyi bitirmek için 'q' veya 'Q' tuşuna basın.")
                task_name = input("Yeni görev ismini girin: ")
                if task_name.lower() == 'q':
                    break
                elif task_name.lower() == 'c':
                    continue
                else:
                    tasks.append({"name": task_name, "done": False})
                    print("Görev başarıyla eklendi.")


        elif choice == "2":
            try:
                task_index = int(input("Tamamlanan görevin numarasını girin: ")) - 1
                tasks[task_index]["done"] = True
            except:
                print("Hatalı giriş.")
                time.sleep(2)

        elif choice == "3":
            try:
                task_index = int(input("Silinecek görevin numarasını girin: ")) - 1
                del tasks[task_index]
            except:
                print("Hatalı giriş.")
                time.sleep(2)
                    
        elif choice == "4":
            # Pomodoro başladı, yapılacaklar listesi gösteriliyor
            os.system('cls')
            print("Pomodoro başladı! Yapılacaklar listesi:")
            for index, task in enumerate(tasks):
                if task["done"]:
                    print(f"{index + 1}. [X] {task['name']} ")
                else:
                    print(f"{index + 1}. [ ] {task['name']} ")
                    


            for i in range(sets):
                for j in range(minutes):
                    os.system('cls')
                    print("Pomodoro başladı! Çalışma zamanı...\n")
                    print(f"Set: {i + 1}/{sets}")
                    print(f"Dakika: {j + 1}/{minutes}")
                    print("\nYapılacaklar Listesi:")
                    for index, task in enumerate(tasks):
                        if task["done"]:
                            print(f"{index + 1}. [X] {task['name']} ")
                        else:
                            print(f"{index + 1}. [ ] {task['name']} ")
                    time.sleep(60)
                start_file = "art.txt"
                with open(start_file) as f:
                    art = f.read()
                os.system('cls')
                print(f"{art}\nPomodoro bitti!\n")

                # Sesli uyarı ve mola süresi
                sound_file = "alarm.wav"
                os.system(f'start "" "{sound_file}"')
                time.sleep(2)
                os.system('cls')
                print("Mola zamanı...\n")
                time.sleep(break_time * 60)


        elif choice == "5":
            try:
                while True:
                    os.system('cls')
                    print("Ayarlar\n")
                    print(f"1. Pomodoro Süresi: {minutes} dakika")
                    print(f"2. Pomodoro Set Sayısı: {sets}")
                    print(f"3. Mola Süresi: {break_time} dakika")
                    print(f"4. Ses Dosyası: {sound_file}")
                    print("5. Geri")
                    sub_choice = input("Yapmak istediğiniz işlemi seçin: ")
                    if sub_choice == "1":
                        minutes = int(input("Yeni pomodoro süresini dakika cinsinden girin: "))
                    elif sub_choice == "2":
                        sets = int(input("Yeni pomodoro set sayısını girin: "))
                    elif sub_choice == "3":
                        break_time = int(input("Yeni mola süresini dakika cinsinden girin: "))
                    elif sub_choice == "4":
                        sound_file = input("Yeni ses dosyasının yolunu girin: ")
                    elif sub_choice == "5":
                        break
                    else:
                        print("Geçersiz seçim, tekrar deneyin.")
                        time.sleep(2) # 2 saniye bekle
            except:
                print("Hatalı giriş.")
                time.sleep(2)

        elif choice == "6":
            break
        else:
            print("Geçersiz seçim, tekrar deneyin.")
            time.sleep(2) # 2 saniye bekle

if __name__ == '__main__':
    main()
