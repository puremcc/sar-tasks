#!/usr/bin/python3

import subprocess
import argparse
from datetime import datetime, timedelta
from typing import List
from twodolib import TwoDoTask


def main():
    args = get_args()

    project_name = f"SAR - {args.mentee_name} - {args.cycle_year} Q{args.cycle_quarter}"
    forList = "Mentoring"

    project = TwoDoTask(
        project_name,
        task_type=1,
        for_list=forList,
        starred=True,
        due=args.delivery_due_date
    )

    tasks = initialize_tasks(args.mentee_name, args.delivery_due_date, args.qa_date)

    # Create project.
    save_task(project)

    # Create tasks.
    for task in tasks:
        task.for_list = forList
        task.forParentName = project_name
        save_task(task)


def save_task(task: TwoDoTask):
    subprocess.call(['open', task.url()])
    return task.get_taskid()


def shift_date(date: str, days=0, weeks=0) -> str:
    shiftedDate = date
    if weeks != 0:
        shiftedDate = datetime.strftime(datetime.strptime(
            shiftedDate, "%Y-%m-%d") + timedelta(weeks=weeks), "%Y-%m-%d")
    if days != 0:
        shiftedDate = datetime.strftime(datetime.strptime(
            shiftedDate, "%Y-%m-%d") + timedelta(days=days), "%Y-%m-%d")
    return shiftedDate


def initialize_tasks(mentee_name, delivery_due_date=None, qa_date=None) -> List[TwoDoTask]:
    return [
        TwoDoTask(
            f"Send email request to {mentee_name} for feedback reviewers list and self-assessment",
            tags="@email",
            due=shift_date(qa_date, weeks=-3) if qa_date else None
        ),
        TwoDoTask(
            f"Send out feedback requests for {mentee_name}'s SAR",
            tags="@email",
            due=shift_date(qa_date, weeks=-3) if qa_date else None
        ),
        TwoDoTask(
            f"Write first draft of {mentee_name}'s SAR",
            tags="@computer",
            due=shift_date(qa_date, weeks=-1) if qa_date else None
        ),
        TwoDoTask(
            f"Complete final draft of {mentee_name}'s SAR",
            tags="@computer",
            priority=TwoDoTask.PRIO_HIGH,
            due=shift_date(qa_date, days=-3) if qa_date else None
        ),
        TwoDoTask(
            f"Write executive summary for {mentee_name}'s QA session",
            tags="@anywhere",
            due=shift_date(qa_date, days=-1) if qa_date else None
        ),
        TwoDoTask(
            f"Incorporate feedback from {mentee_name}'s QA session",
            tags="@computer",
            start=f"{qa_date} 08:00" if qa_date else None,
            due=shift_date(qa_date, days=1) if qa_date else None
        ),
        TwoDoTask(
            f"Deliver {mentee_name}'s SAR",
            tags="@anywhere",
            start=f"{shift_date(qa_date, days=1)} 08:00" if qa_date else None,
            due=delivery_due_date
        )
    ]


def get_args():
    parser = argparse.ArgumentParser(
        description='Create SAR project and subtasks in 2Do.')
    parser.add_argument("mentee_name", help="Mentee's Name")
    parser.add_argument("cycle_year", type=int, help="Review cycle year")
    parser.add_argument("cycle_quarter", metavar='cycle_quarter', type=int, choices=range(1, 5),
                        help="Review cycle quarter [1-4]")
    parser.add_argument("-q", "--qa-date",
                        help='Date of QA session [yyyy-mm-dd]')
    parser.add_argument("-d", "--delivery-due-date",
                        help='Due date to deliver the review [yyyy-mm-dd]')
    return parser.parse_args()


if __name__ == "__main__":
    main()
