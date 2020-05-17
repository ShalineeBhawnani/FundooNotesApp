import { Component, OnInit } from '@angular/core';
import { Events } from 'src/app/models/eventModel';

@Component({
  selector: 'app-reminder',
  templateUrl: './reminder.component.html',
  styleUrls: ['./reminder.component.scss']
})
export class ReminderComponent implements OnInit {
  minDate=new Date();
  dayCount:number=0;
  timeCount:number=0;
  reminder:any;
  event:Events;
  reminderList = [
    {Day: "Later Today", Time: "20:00", dayCount: 0, timeCount: 20 },
    {Day: "Tomorrow", Time: "08:00", dayCount: 1, timeCount: 8},
    {Day: "Next Week", Time: "08:00", dayCount: 7, timeCount: 8 }
  ]
  timeList = [
    { title: "Morning", time: "08:00",timeCount:8,dayCount:0 },
    { title: "AfterNoon", time: "13:00",timeCount:13,dayCount:0 },
    { title: "Evening", time: "18:00",timeCount:18,dayCount:0 },
    { title: "Night", time: "20:00",timeCount:20,dayCount:0 }]
    timeSelected:any;
  constructor() { }

  ngOnInit() {
  }

}
