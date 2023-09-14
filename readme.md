<div align="center">
     <img src="https://github.com/MFINUE/.github/raw/main/profile/assets/logo.png" height=70>
     <h1>Niepce</h1>
</div>

A util to identify, to distinguish, and to tag each photo taken during [the MFINUE Conference](https://mfinue.org).
## Usage

Create two folders at the root of of the project: 

- `images` should hold all the input images whose faces will be tagged
- `keys` should serve as a parent directory to your key images. Each key image should be a distinct folder and contain at least one picture of that person's face<br>
 
Now the new directory tree shold be looking like this:
```
📂 niepce
 ├─── 📂 images
 |    └─── 📷 image1.png
 └─── 📂 keys
      ├─── 📂 person1
      |    ├─── 📷 key1.png
      |    └─── 📷 key2.png
      └───📂 person2
          └───...
```

Run the following command to execute the script

```sh
$ python . ./images --keys ./keys
```


The results should appear in a freshly created folder `out`