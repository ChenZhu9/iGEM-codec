# iGEM-codec
This is a codec for our bio-storage
We achieve the highest fault tolerance with minimal redundancy by encoding our data to Galois field and decoding them with Reed-Soloman algorithm. However, such calculations are very large for researchers, so we need to develop a codec to encode the data into a 96-well plate and read the 96-well plate and decode it into the data we need.

What's more, in a practical way, with panels seeded with our engineered bacteria, information transformed into QR-code can be recorded by adding inducer to dots that are black. Information can be easily extract by scanning the plate by a microplate reader. 
