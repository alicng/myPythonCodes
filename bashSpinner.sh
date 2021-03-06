#!/bin/bash
 
clear
#spinner=( Ooooo oOooo ooOoo oooOo ooooO oooOo ooOoo oOooo);
spinner=( '|' '/' '-' '\');
cat << EOF
Hello.
Thank you for trying this script out.
I will now wait 10 seconds,
but you will see a "spinner"
as a visual for the user.
EOF
 
 
count(){
  echo "Copying files"
  spin &
  pid=$!
 
  for i in `seq 1 10`
  do
    sleep 1;
  done
 
  kill $pid  
}
 
spin(){
  while [ 1 ]
  do 
    for i in ${spinner[@]}; 
    do 
      echo -ne "\r$i";
      sleep 0.2;
    done;
  done
}
 
count