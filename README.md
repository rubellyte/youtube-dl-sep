﻿# Report for Assignment 1

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

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>
get_suitable_downloader
<Provide the same kind of information provided for Function 1>

#### Jordan Smith

formatSeconds: [Instrumentation](https://github.com/rubellyte/youtube-dl-sep/commit/c11880381c947136ba251914cf5b943dfa331675)

Result from existing tests:

![Instrumentation result from existing tests](coverage_format_seconds_before.png)

format_bytes: [Instrumentation](https://github.com/rubellyte/youtube-dl-sep/commit/9a24bc632543ca3642759776b3113a0989fccc6a)

Result from existing tests:

![Instrumentation result from existing tests](coverage_format_bytes_before.png)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>
test_get_base_url
<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>
test_get_suitable_downloader
<Provide the same kind of information provided for Test 1>

#### Jordan Smith

TestFormatSeconds: [New tests](https://github.com/rubellyte/youtube-dl-sep/commit/2a1cfe97089a3b40f4b36de4784cba7fcf5add2a)

Before:

![Instrumentation result from existing tests](coverage_format_seconds_before.png)

After:

![Instrumentation result from new tests](coverage_format_seconds_after.png)

TestFormatBytes: [New tests](https://github.com/rubellyte/youtube-dl-sep/commit/f9d8f719a5c0a8c13c8a63223d5db1d28681628d)

Before:

![Instrumentation result from existing tests](coverage_format_bytes_before.png)

After:

![Instrumentation result from new tests](coverage_format_bytes_after.png)


### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
