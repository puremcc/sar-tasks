# sar-tasks

Generate projects and tasks in 2Do app for upcoming Semiannual Reviews (SARs).

## Usage

```txt
usage: create_sar_tasks_in_2do.py [-h] [-q QA_DATE] [-d DELIVERY_DUE_DATE] mentee_name cycle_year cycle_quarter

Create SAR project and subtasks in 2Do.

positional arguments:
  mentee_name           Mentee's Name
  cycle_year            Review cycle year
  cycle_quarter         Review cycle quarter [1-4]

optional arguments:
  -h, --help            show this help message and exit
  -q QA_DATE, --qa-date QA_DATE
                        Date of QA session [yyyy-mm-dd]
  -d DELIVERY_DUE_DATE, --delivery-due-date DELIVERY_DUE_DATE
                        Due date to deliver the review [yyyy-mm-dd]
```

## Demo

![Demo](create_sar_tasks_demo.gif)
