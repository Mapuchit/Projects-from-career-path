 ## String Methods project
 ## Casual Coded Correspondence

'''
In this project, you will be working to code and decode various messages between you and your fictional cryptography enthusiast pen pal Vishal.
'''

## Decode Vishal's Message

alphabet = "abcdefghijklmnopqrstuvwxyz"
offset = 10
secret_message = '''
xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh.
muhu oek qrbu je tusetu yj?
y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!
'''

def decoder(message, offset):
    decoded_message = ""
    for ch in message:
        if ch not in alphabet:
            # add to new message as it is
            decoded_message += ch
        else:
            # find the index of ch in alphabet
            ch_index = alphabet.find(ch)
            # shift index to the RIGHT by the offset to decode the message (opposite action to coding)
            # we divide by len(alphabet) to account for shifts past the end of the alphabet
            new_ch_index = (ch_index + offset) % len(alphabet)
            # add to new message
            decoded_message += alphabet[new_ch_index]
    return decoded_message

print(decoder(secret_message, offset))

## Send Vishal a Coded Message

my_message = '''
hi vishal! that was great fun!
though it took me a while to realise that i have to shift the characters to the right and not to the left,
because you have already shifted them to the left whem coding the message.
so it took a bit of frustration to figure out. but i did it.
'''

def coder(message, offset):
    coded_message = ""
    for ch in message:
        if ch not in alphabet:
            coded_message += ch
        else:
            ch_index = alphabet.find(ch)
            # shift index to the left by the offset to code the message
            new_ch_index = ch_index - offset
            # add to new message
            coded_message += alphabet[new_ch_index]
    return coded_message

print(coder(my_message, offset))

# try to decode to check if coding was successful
coded_message = '''
xy lyixqb! jxqj mqi whuqj vkd!
jxekwx yj jeea cu q mxybu je huqbyiu jxqj y xqlu je ixyvj jxu sxqhqsjuhi je jxu hywxj qdt dej je jxu buvj,
rusqkiu oek xqlu qbhuqto ixyvjut jxuc je jxu buvj mxuc setydw jxu cuiiqwu.
ie yj jeea q ryj ev vhkijhqjyed je vywkhu ekj. rkj y tyt yj.
'''
print(decoder(coded_message, offset))

## Decodint more messages

first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
print(decoder(first_message, offset))

second_message = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"
offset = 14
print(decoder(second_message, offset))

## Solving a Caesar Cipher without knowing the shift value

# Brute force it!
latest_message = '''
vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx.
px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.
'''
# try every offset from 1 to 10
offset = [n for n in range(1, 11)]

for n in offset:
    print("offset:" + str(n))
    print(decoder(latest_message, n))

# we found the offset! #7

## The Vigenère Cipher

# first we try to code a message with a known coded form to see how it works
# and then we can reverse the process to decode
trial_message = "barry is the spy"
trial_keyword = "dog"
# we should get after coding: "eoxum ov hnh gvb"
alphabet = "abcdefghijklmnopqrstuvwxyz"

print("Trying vigenere_coder:")

def vigenere_coder(message, keyword):
    # generate the keyword_phrase
    keyword_phrase = ""
    # a list of keys from keyword in reverse order for ease of iteration an pop()
    keys = [ch for ch in keyword[::-1]]
    for ch in message:
        if ch not in alphabet:
            keyword_phrase += ch
        else:
            if len(keys) > 0:
                keyword_phrase += keys.pop()
            else:
                # reset the keys list to restart the iteration over the keyword
                keys = [ch for ch in keyword[::-1]]
                keyword_phrase += keys.pop()

    # print(keyword_phrase)
    # should print "dogdo gd ogd ogd"

    # finding the new place values and encoding the message
    coded_message = ""
    for i in range(len(message)):
        if keyword_phrase[i] not in alphabet:
            coded_message += keyword_phrase[i]
        else:
            original_value = alphabet.find(message[i])
            added_value = alphabet.find(keyword_phrase[i])
            new_value = (original_value + added_value) % len(alphabet)
            coded_message += alphabet[new_value]

    return coded_message

print(vigenere_coder(trial_message, trial_keyword))
# should print "eoxum ov hnh gvb"


print("Trying vigenere_decoder:")

def vigenere_decoder(message, keyword):
    # find the keyword_phrase
    keyword_phrase = ""
    keys = [ch for ch in keyword[::-1]]
    for ch in message:
        if ch not in alphabet:
            keyword_phrase += ch
        else:
            if len(keys) > 0:
                keyword_phrase += keys.pop()
            else:
                # reset the keys list to restart the iteration over the keyword
                keys = [ch for ch in keyword[::-1]]
                keyword_phrase += keys.pop()

    # print(keyword_phrase)
    # should print "dogdo gd ogd ogd"

    # finding the original place values and decode the message
    decoded_message = ""
    for i in range(len(message)):
        if keyword_phrase[i] not in alphabet:
            decoded_message += keyword_phrase[i]
        else:
            coded_value = alphabet.find(message[i])
            added_value = alphabet.find(keyword_phrase[i])
            new_value = coded_value - added_value
            decoded_message += alphabet[new_value]

    return decoded_message

# try with the example message first
trial_coded_message = "eoxum ov hnh gvb"

print(vigenere_decoder(trial_coded_message, trial_keyword))
# should print "barry is the spy"

print("\nDecoding the message sent with Vigenère Cipher:")

tough_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
new_keyword = "friends"

print(vigenere_decoder(tough_message, new_keyword))

## Send a message with the Vigenère Cipher

message_to_vishal = "that's enough for today. i'm quite proud of myself."
my_keyword = "python"

print("\nThe coded message as sent to Vishal:")
print(vigenere_coder(message_to_vishal, my_keyword))

message_received = "ifta'g rcmnnv sdp mvrnn. g'f xivic iychs my tmftjy."

print("\nDecoded:")
print(vigenere_decoder(message_received, my_keyword))
