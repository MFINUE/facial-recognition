<div align="center">
     <img src="https://github.com/MFINUE/.github/raw/main/profile/assets/logo.png" height=70>
     <h1>Niepce</h1>
</div>

## Usage:
- Create a images directory where you will put your images Ex: `.\images`
- Create a keys directory where your photo keys will be stored Ex: `.\keys`. For each person don't forget create a new sub-directory
 
- Now the new directory tree shold be looking like this:
   ```
    .
    ├───images
    |   └───...
    └───keys
        ├───person1
        |   └───...
        └───person2
            └───...
    
    ```

- You may go ahead and run the script by using `python main.py .\images --keys .\keys`
- This will produce an `.\out` folder with the pictures of each person