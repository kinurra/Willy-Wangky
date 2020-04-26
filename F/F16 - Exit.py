def exit():
     close = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")

     while (not close == 'Y' or not close == 'N'):
          close = input("Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ")

     if (close == "Y"):
          save_file()
          username = login_user()

     else:
          file = load()
          username = login_user()

          
