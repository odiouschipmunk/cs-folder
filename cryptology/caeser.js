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