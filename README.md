# Report for Assignment 1

## Project chosen

Name: youtube-dl

URL: (https://github.com/ytdl-org/youtube-dl)

Number of lines of code and the tool used to count it: 142,738 LOC reported by `lizard`

Programming language: Python

## Coverage measurement

### Existing tool

`coverage.py` was used to check existing coverage. The command run was `coverage run --branch -m unittest discover`.

![Coverage report before changes](coverage_before.png)

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>
Nikitas Konstantopoulos
<Function 1 name>

get_base_url
<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

https://github.com/rubellyte/youtube-dl-sep/commit/fe2c02649b2105fcf4fe2cfa45de8182aa6f23e4
<Provide a screenshot of the coverage results output by the instrumentation>

Old Coverage Results:     ![Initial coverage for __init__.py](inital_coverage_init_.png)    
<Function 2 name>
get_suitable_downloader
<Provide the same kind of information provided for Function 1>
https://github.com/rubellyte/youtube-dl-sep/commit/dba5d4863c23ff483fd4cc035a85dd9624819d1b

Old Coverage Results:     ![Initial coverage for f4m.py](inital_coverage_f4m.png)    


## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

Nikitas Konstantopoulos
<Test 1>

test_get_base_url
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

https://github.com/rubellyte/youtube-dl-sep/commit/4608aad7a7522b296174b4c56d66adfac6fc20ee
<Provide a screenshot of the old coverage results (the same as you already showed above)>

Old Coverage Results:     ![Initial coverage for f4m.py](inital_coverage_f4m.png)    
<Provide a screenshot of the new coverage results>

New Coverage Results:     ![Renewed coverage for f4m.py](final_coverage_f4m.png)    

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

test_get_suitable_downloader
<Provide the same kind of information provided for Test 1>

https://github.com/rubellyte/youtube-dl-sep/commit/59165134c15a5982a548b2db68ec24449b1b47f1

Old Coverage Results:     ![Initial coverage for __init__.py](inital_coverage_init_.png)    

New Coverage Results:     ![Renewed coverage for __init__.py](final_coverage_init_.png)    

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

Old Coverage Results of __init__.py:     ![Initial coverage for __init__.py](inital_coverage_init_.png)    

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

New Coverage Results of __init__.py:     ![Renewed coverage for __init__.py](final_coverage_init_.png)    

## Statement of individual contributions

<Write what each group member did>

Nikitas Konstantopoulos: Instrumented the get_suitable_downloader function and created a test for it(improved coverage for the function) and Instrumented the get_base_url function and created a test for it (improved coverage for the function) 