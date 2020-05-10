# Multiquestion answering

## Student.ai

Main algorithm used is word2vec

other parts of code are contributed by [This guy](https://github.com/stanleyfok)

What do you need to run

 first
 
```pip install -r requirements.txt```
 
 second
 
 copy all lectures of the subject (including a book) to the directory ```study_material```
 and create an empty directory called ```data```
 then
 
 run the following script
 
 ```shell script
  ls ./study_material > ./study_material/filenames.txt
```
 
 open the jupyter notebook and tweak the parameters or leave as is
 
 ```python

concat_title = True
window = 5 # how many pages you want to include in one doc
book_included = False
booktitle = 'thebook' # if you have abook this is its name
exampath = './midterm exam/Midterm exam.html' # if you want to check



```


then run all cells
