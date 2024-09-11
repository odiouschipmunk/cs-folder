/*****************************************************************************
 * Write a program that asks the user for an encrypted message 
 * and Caesar cipher key, and decrypts the message.
 *
 * To do this, find the function caesarEncrypt! Read through it to figure out
 * how the message is encrypted. Then, find the function caesarDecrypt. Can 
 * you reverse the method to decrypt the message??
 *
 ******************************************************************************/

var ALPHABET = "abcdefghijklmnopqrstuvwxyz";

// caesarEncrypt function 
function caesarEncrypt(message, key){
    var encryptedResult = "";
    
    // Goes through the message to encrypt one letter at a time
    for(var i = 0; i < message.length; i++){
        var originalCharacter = message.charAt(i);
        
        // Finds where each letter is in the ALPHABET
        var alphabeticIndex = ALPHABET.indexOf(originalCharacter);
        
        // As long as it exists in the ALPHABET...
        if(alphabeticIndex >= 0){
            
            // Shifts the letter to the RIGHT according to the key.
            
            // Advanced: It also adds the length of the alphabet (26)
            // and divides by the length to account for wrapping around to the 
            // beginning when needed
            var newIndex = alphabeticIndex + key + ALPHABET.length;
            newIndex = newIndex % ALPHABET.length;
            
            // Get the new letter
            var newCharacter = ALPHABET.charAt(newIndex);
            
            // Add the new shifted letter to the encrypted result
            encryptedResult += newCharacter
        }
        
        // If it's not in the ALPHABET (like punctuation), keep the original 
        // character
        else{
            encryptedResult += originalCharacter;
        }
    }
    
    return encryptedResult;
}

// caesarDecrypt function 
function caesarDecrypt(message, key){
    var decryptedResult = "";
    
    // Goes through the message to decrypt one letter at a time
    for(var i = 0; i < message.length; i++){
        var originalCharacter = message.charAt(i);
        
        // Finds where each letter is in the ALPHABET
        var alphabeticIndex = ALPHABET.indexOf(originalCharacter);
        
        // As long as it exists in the ALPHABET...
        if(alphabeticIndex >= 0){
            
            // Shifts the letter to the LEFT according to the key.
            
            // Advanced: It also adds the length of the alphabet (26)
            // and divides by the length to account for wrapping around to the 
            // beginning when needed
            var newIndex = alphabeticIndex - key + ALPHABET.length;
            newIndex = newIndex % ALPHABET.length;
            
            // Get the new letter
            var newCharacter = ALPHABET.charAt(newIndex);
            
            // Add the new shifted letter to the decrypted result
            decryptedResult += newCharacter
        }
        
        // If it's not in the ALPHABET (like punctuation), keep the original 
        // character
        else{
            decryptedResult += originalCharacter;
        }
    }
    
    return decryptedResult;
}

// Run Program
function start(){
    
    // Takes a message from the user and changes it to all lowercase letters
    var originalMessage = readLine("Enter the message you would like to encrypt: ");
    originalMessage = originalMessage.toLowerCase();
    
    // Takes a secret key from the user
    var secretKey = readInt("Enter the number you'd like to shift each character by: ");
    
    // Encrypts the message using the caesarEncrypt function
    var encryptedMessage = caesarEncrypt(originalMessage, secretKey);
    println("");
    println("Encrypted message: " + encryptedMessage);
    
    println("");
    println("Decrypting message...");
    println("");
    
    // Decrypts the message using the caesarDecrypt function
    var decrypted = caesarDecrypt(encryptedMessage, secretKey);
    println("Done:");
    
    println(decrypted);
}

