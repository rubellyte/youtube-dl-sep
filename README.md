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

#### Jordan Smith

**Function 1: formatSeconds**

[Instrumentation](https://github.com/rubellyte/youtube-dl-sep/commit/c11880381c947136ba251914cf5b943dfa331675)

Result from existing tests:

![Instrumentation result from existing tests](coverage_format_seconds_before.png)

**Function 2: format_bytes**

[Instrumentation](https://github.com/rubellyte/youtube-dl-sep/commit/9a24bc632543ca3642759776b3113a0989fccc6a)

Result from existing tests:

![Instrumentation result from existing tests](coverage_format_bytes_before.png)

#### Nikitas Konstantopoulos

**Function 1: get_base_url**

[Instrumentation](https://github.com/rubellyte/youtube-dl-sep/commit/fe2c02649b2105fcf4fe2cfa45de8182aa6f23e4)

Old Coverage Results:
![Initial coverage for f4m.py](inital_coverage_f4m.png)

**Function 2: get_suitable_downloader**

[Instrumentation](https://github.com/rubellyte/youtube-dl-sep/commit/fe2c02649b2105fcf4fe2cfa45de8182aa6f23e4)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

#### Jordan Smith

**Test 1: TestFormatSeconds**

[New tests](https://github.com/rubellyte/youtube-dl-sep/commit/2a1cfe97089a3b40f4b36de4784cba7fcf5add2a)

Before:

![Instrumentation result from existing tests](coverage_format_seconds_before.png)

After:

![Instrumentation result from new tests](coverage_format_seconds_after.png)

**Test 2: TestFormatBytes**

[New tests](https://github.com/rubellyte/youtube-dl-sep/commit/f9d8f719a5c0a8c13c8a63223d5db1d28681628d)

Before:

![Instrumentation result from existing tests](coverage_format_bytes_before.png)

After:

![Instrumentation result from new tests](coverage_format_bytes_after.png)

#### Nikitas Konstantopoulos

**Test 1: test_get_base_url**

[New/enhanced test](https://github.com/rubellyte/youtube-dl-sep/commit/4608aad7a7522b296174b4c56d66adfac6fc20ee)

Old Coverage Results:
![Initial coverage for f4m.py](inital_coverage_f4m.png)

New Coverage Results:
![Renewed coverage for f4m.py](final_coverage_f4m.png)

**Test 2: test_get_suitable_downloader**

[New/enhanced test](https://github.com/rubellyte/youtube-dl-sep/commit/4608aad7a7522b296174b4c56d66adfac6fc20ee)

## Coverage improvement

### Overall

Old Coverage Results of __init__.py:
![Initial coverage for __init__.py](inital_coverage_init_.png)

New Coverage Results of __init__.py:
![Renewed coverage for __init__.py](final_coverage_init_.png)

## Statement of individual contributions

<Write what each group member did>
