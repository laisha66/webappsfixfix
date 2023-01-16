import streamlit as st


st.image ("https://s4.aconvert.com/convert/p3r68-cdx67/aksml-vpvh1.jpg",width=650)
    
st.title('Aplikasi penentuan pH suatu larutan')  
st.markdown('''Hai users, selamat datang di web kami. 
Aplikasi ini dapat digunakan untuk teman-teman yang sedang mengerjakan analisis dengan parameter penentuan nilai pH dari suatu larutan atau sampel.''')


tombol=st.button('OLEH KELOMPOK 3')
if tombol:
    st.write('Laisha Awiana Maharani')
    st.write('Muhammad Ridwan')
    st.write('Putra Harapan Mahmuddin')
    st.write('Salwaa Nuhaa Nazhira')
    st.write('Siti Nur Aziizah Rustam')

tab1, tab2, tab3, tab4 = st.tabs(["pH scale", "Equipment", "How to","Penentuan nilai pH"])

with tab1:
   st.header("pH scale")
   st.image("https://s4.aconvert.com/convert/p3r68-cdx67/aud98-igj3m.jpg", width=500)

with tab2:
   st.header("Equipment")
   st.write ('Berikut adalah alat-alat yang dapat digunakan untuk mengukur pH suatu larutan:')
   st.image("https://s4.aconvert.com/convert/p3r68-cdx67/ask5h-0p4km.jpg", width=350, caption='pH meter')
   st.image ("https://s4.aconvert.com/convert/p3r68-cdx67/a7pn5-x3f8r.jpg",width=350, caption='pH universal')
   st.image ('https://s4.aconvert.com/convert/p3r68-cdx67/adu8m-xrxeg.jpg',width=350, caption='kertas lakmus')

with tab3:
   st.header("How to use the equipment")
   st.write ('''A. pH Meter: 
1. Disiapkan sampel yang akan di ukur kadar pHnya (letakkan dalam wadah).  
2. Dinyalakan dengan menekan tombol on pada pH meter.  
3. Dimasukkan pH meter ke dalam wadah yang berisi sampel/larutan yang akan di uji.   
4. Ditunggu hingga angka tersebut berhenti dan tidak berubah-ubah.  
5. Hasil akan terlihat di display digital.

B. pH universal: 
1. Disiapkan sampel yang akan di ukur kadar pHnya (letakkan dalam wadah). 
2. Dimasukkan pH universal kedalam larutan yang akan di uji.
3. Dibandingkan dengan skala yang terdapat pada tempat kertas pH universal
4. Didapatkan pH dari larutan tersebut

C. Kertas Lakmus:
Kertas lakmus hanya dapat mengetahui apakah suatu larutan tersebut basa atau asam. Kita tidak dapat mengetahui berapa pH dari larutan tersebut.
''')

with tab4:
   st.header("Penentuan nilai pH")

   NamaLarutan= st.text_input('Nama Larutan yang akan dihitung pH-nya:')

   st.write ('Silahkan pilih jenis larutan dengan format "asam kuat","basa kuat","asam lemah","basa lemah"')

   option= st.selectbox(
   'Jenis larutan',
   ('asam kuat','basa kuat','asam lemah','basa lemah'))

   if option=="asam kuat":
         jumlah_digit=4
         cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
         jumlah_digit1=0
         val = st.number_input(f'Masukan valensi larutan',format='%.'+str(jumlah_digit1)+'f')
         H=cons*val
         import numpy as np
         pH= -1 * np.log10(H)
         st.write('pH larutan',NamaLarutan,'adalah',pH)
    
   elif option == "basa kuat":
        jumlah_digit=4
        cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
        jumlah_digit1=0
        val = st.number_input(f'Masukan valensi larutan',format='%.'+str(jumlah_digit1)+'f')
        OH=cons*val 
        import numpy as np
        pOH= -1 * np.log10(OH)
        pH=14-pOH
        st.write('pH larutan',NamaLarutan,'adalah',pH)
    
   elif option == "asam lemah":
        jumlah_digit=4
        cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
        jumlah_digit1=6
        ka = st.number_input(f'Masukan ka dari larutan',format='%.'+str(jumlah_digit1)+'f')
        a = cons * ka
        import numpy as np
        H = np.sqrt(a)
        pH= -1 * np.log10(H)
        st.write('pH larutan',NamaLarutan,'adalah',pH)
    
   elif option == "basa lemah":
        jumlah_digit=4
        cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
        jumlah_digit1=6
        kb = st.number_input(f'Masukan kb dari larutan',format='%.'+str(jumlah_digit1)+'f')
        a = cons * kb
        import numpy as np
        OH = np.sqrt(a)
        pOH= -1 * np.log10(OH) 
        pOH= -1 * np.log10(OH)
        pH=14-pOH
        st.write('pH larutan',NamaLarutan,'adalah',pH)
    
   st.image ("https://s4.aconvert.com/convert/p3r68-cdx67/a1yn7-thob6.jpg",width=500)




    
    
    
