requirements.txt dosyasında python kodlarını çalıştırmak için gerekli kütüphaneler bulunmaktadır.
pip install -r requirements.txt komutu ile kütüphaneleri yükleyebilirsiniz.
anaconda kullanıyorsanız yeni bir environment oluşturup, environment adı yezan yere environment adını yazarsanız. İlgili kütüphaneler yüklenecektir.
conda install --force-reinstall -y -q --name [environment_adı] -c conda-forge --file requirements.txt