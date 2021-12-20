# Weak Salt
## Theory
Let's assume Alice and Bob found a way how to make university labs fast and easily. They need secure communication, so they generate a key and transfer it in a secure way. Now, they decide to encrypt their messages with Salsa20 algorithm with no nonce, which basically means:

> encrypted_message = message ^ key.

This seems good, however when using the same key for every message, this can be easily broken. Let's use some math:

> encrypted_message1 ^ encrypted_message2 = (message1 ^ key) ^ (message2 ^ key)
> 
> (message1 ^ key) ^ (message2 ^ key) = message1 ^ message2

Sounds complicated, so let's encrypt some images to show this type of attack:

![Image explanation](https://github.com/KotesUA/Security/tree/master/WeakSalt/Explanation.jpg?raw=true)

So, as we can see with these images, it's quite easy to decode this type of encryption, using 2 messages with the same key.

## Time to practice
So, our task is to recover a set of 18 HEX strings, encrypted with the same key. We know, that it is a single piece of literature, so we cane perform advanced Google search on recovered fragments to find all text.

Firstly, we XOR first line with each other line in the set to have a complete picture.

Then, for each row, we Xor it with different English words, that are popular: "the", "is", "are", "who" and so on. As for "For the", we have this output:
> Th'ospx
> 
>The sad
> 
>The jny
> 
>That#pk
> 
>When#ho
> 
>With#a*
> 
>To gqud
> 
>But whk
> 
>The vnn
> 
>No tqa|
> 
>And naa
> 
>Than#ff
> 
>Thus#ce
> 
>And wh
> 
>Is sjca
> 
>And fn~
> 
>With#tb

And then we're just keep combining these words, spaces and different cases to retrieve more. Somewhere in these attempts we saw a result "Than fly ", which seems to be a true part of the text, so XORing on this brought us to a phrase "Than fly", which is obviously must be "Than fly to ", which gave us all first words in the text.

Searching for exact match for "The pangs of" led us to a full string of William Shakespear's Hamlet:
![Key moment](https://github.com/KotesUA/Security/tree/master/WeakSalt/Google.png?raw=true)

Now, inserting this string into our algorythm, we can easily decrypt the text, using XOR on the third line and the decrypted fragment.