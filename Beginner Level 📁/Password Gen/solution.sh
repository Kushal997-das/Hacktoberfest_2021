#!/bin/bash

echo "Selamat datang di password generator"

echo "Mohon Masukan panjang password yang akan ada buat!"

read PASS_LENGTH

if ! [[ $PASS_LENGTH =~ ^[0-9]+$ ]]; then
    echo "error: mohon isi dengan nomor yang valid"
    exit 1
fi
password ds=()

for p in $(seq 1 3);
do
    passwords+=("$(openssl rand -base64 48 | cut -c1-$PASS_LENGTH )")
done 

echo "Ini password yang sudah di generate:"
printf "%s\n" "${passwords[@]"

echo "apakah kamu ingin menimpan password ini? (y/n)"
read choice
if [ "$choice" = "y" ]; then

        for password in "${passwords[@]}"; do

            echo "$passwords" | ccrypt -e -K "$PASSPHARSE" > "password.txt.cpt"
        done
    
    echo "password tersimpan! ke password.txt.cpt"

elif [ "$choice" = "n" ]; then
    echo "password tidak tersimpan"
fi