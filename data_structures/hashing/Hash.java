/************************************************
 Open Address Hashing
 Objective: empirically evaluate the 3 open addressing approaches when a hashing table is about 90% full.

 Open Addressing methods:
        LINEAR PROBING:
        h(k, i) = (h'(k) + i) mod(m)
            where
            h'(k) = k

        QUADRATIC PROBING:
        h(k, i) = (h'(k) + c1*i + c2*i^2) mod(m)
            where
            h'(k) = k, c1 = 1, c2 = 3

        DOUBLE HASHING:
        h(k, i) = ( h1(k) + ih2(k) ) mod(m)
            where
            h1(k) = k
            h2(k) = 1 + (k mod(m-1) )
************************************************/
import java.util.ArrayList;
import java.util.Random;

public class Hash
{
    private static int m;// length m of table
    private static int quantity;// quantity to insert
    private static int[] hashTable;// create new hash tables for each hash method
    private static ArrayList<Integer> values;// list with unique pre-generated values

    //===========================================
    // Constructor
    //===========================================
    private Hash(int m, int quantity)
    {
        this.m = m;
        this.quantity = quantity;
        values = new ArrayList<>();
        addValues();
    }

    //===========================================
    // Insert unique values into the values list, now we can test the three open addressing
    //===========================================
    void addValues()
    {
        for(int i = 0; i < quantity + 950; i++)
        {
            generateUniqueKey();
        }
    }

    private static void generateUniqueKey()
    {
        Random r = new Random();
        int k = r.nextInt(100000) + 1;

        // Check if new random value is not already in the list
        while(checkInArray(k))
        {
            k = r.nextInt(100000) + 1;
        }

        values.add(k);
    }

    //===========================================
    // Check if an element is already in an array (avoid duplicate values )
    //===========================================
    private static boolean checkInArray(int k)
    {
        for(int i = 0; i < values.size(); i++)
        {
            if(values.get(i) == k)
            {
                return true;
            }
        }
        return false;
    }

    //===========================================
    // Auxiliary hash functions h1 and h2
    //===========================================
    private static int hash1(int k)
    {
        return k % m;
    }

    private static int hash2(int k)
    {
        return 1 + (k % (m - 1));
    }

    //===========================================
    // Linear probing method
    //===========================================
    private static int calculateLinearProbing()
    {
        // Create a new hash table to test linear probing
        hashTable = new int[m];
        int count = 0;

        for(int i = 0; i < quantity; i++)
        {
            int k = values.get(i);
            int hashKey = hash1(k);

            if(hashTable[hashKey] == 0)
            {
                hashTable[hashKey] = k;
            }
            else
            {
                int j = 1;
                hashKey = (hash1(k) + j) % m;

                while(hashTable[hashKey] != 0)
                {
                    // Increase count of probes every time there's a collision
                    if(i >= 900)
                    {
                        count++;
                    }

                    j++;
                    hashKey = (hash1(k) + j) % m;
                }

                // Insert k at available index
                hashTable[hashKey] = k;
            }
        }

        return count;
    }

    //===========================================
    // Quadratic probing method
    //===========================================
    private static int calculateQuadraticProbe()
    {
        // Create a new hash table to test quadratic probing
        hashTable = new int[m];
        int count = 0;
        int c1 = 1;
        int c2 = 3;

        for(int i = 0; i < quantity; i++)
        {
            // Get key k and generate hash for index
            int k = values.get(i);
            int hashKey = hash1(k);

            // Insert into index hashKey if no collision
            if(hashTable[hashKey] == 0)
            {
                hashTable[hashKey] = k;
            }
            else
            {
                int j = 1;
                hashKey = (hash1(k) + (j*c1) + (j*j*c2)) % m;

                while(hashTable[hashKey] != 0)
                {
                    // Increase count of probes every time there's a collision
                    if(i >= 900)
                    {
                        count++;
                    }

                    j++;
                    hashKey = (hash1(k) + (j*c1) + (j*j*c2)) % m;
                }

                // Insert k at available index
                hashTable[hashKey] = k;
            }
        }

        return count;
    }

    //===========================================
    // Double hashing method
    //===========================================
    private static int doubleHash(int k, int i)
    {
        return (hash1(k) + (i * hash2(k))) % m;
    }

    // Insert values
    private static int calculateDoubleHash()
    {
        // Create a new hash table to test double hashing
        hashTable = new int[m];
        int count = 0;

        for(int i = 0; i < quantity; i++)
        {
            // Get key k and generate hash for index
            int k = values.get(i);
            int hashKey = hash1(k);

            // Insert if no collision
            if(hashTable[hashKey] == 0)
            {
                hashTable[hashKey] = k;
            }
            else
            {
                // Keep calculating an index that will not cause a collision
                int j = 1;
                int newHashKey = doubleHash(k, j);

                while(hashTable[newHashKey] != 0)
                {
                    // Count probes after adding 900 values
                    if(i >= 900)
                    {
                        count++;// increase count of probes every time there's a collision
                    }

                    j++;
                    newHashKey = doubleHash(k, j);
                }

                // Insert k at available index
                hashTable[newHashKey] = k;
            }
        }

        return count;
    }

    //===========================================
    // Test the three open addressing approaches
    //===========================================
    public static void testOpenAddressing()
    {
        int lProbingProbes = calculateLinearProbing();
        System.out.println("Linear Probing probes: " + lProbingProbes);

        int qProbingProbes = calculateQuadraticProbe();
        System.out.println("Quadratic Probing probes: " + qProbingProbes);

        int doubleHashProbes = calculateDoubleHash();
        System.out.println("Double Hashing probes: " + doubleHashProbes);
    }

    //===========================================
    // Print array
    //===========================================
    private static void print(int[] hashTable, int count)
    {
        for(int i = 0; i < m; i++)
        {
            System.out.println(i + ": " + hashTable[i]);

            if(hashTable[i] != 0)
            {
                count++;
            }
        }
    }

    //===========================================
    // MAIN
    //===========================================
    public static void main(String[] args)
    {
        Hash test = new Hash(1009, 950);
        test.testOpenAddressing();
    }
}
