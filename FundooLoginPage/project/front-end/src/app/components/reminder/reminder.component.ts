import { Component, OnInit,EventEmitter,Output } from '@angular/core';
import { Events } from 'src/app/models/eventModel';
import { FormControl } from '@angular/forms';
import { UserService } from '../../services/user.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { DataService } from '../../services/data.service';


@Component({
  selector: 'app-reminder',
  templateUrl: './reminder.component.html',
  styleUrls: ['./reminder.component.scss']
})
export class ReminderComponent implements OnInit {
  pickedDate = new FormControl(new Date());
  minDate=new Date();
  dayCount:number=0;
  timeCount:number=0;
  reminder:any;
  event:Events;
  @Output() eventCarrier = new EventEmitter<Events>()
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
  constructor(private userService: UserService,
    private snackBar:MatSnackBar,
    private dataService:DataService) { }

  ngOnInit() {
  }

  reminderAdd(reminder){
    //console.log("this is picked date"+this.pickedDate,"this is picked time",this.timeSelected,this.note['id'] )
    //this.timeCount=this.timeSelected
    let data={
      
      "reminder": new Date(this.pickedDate.value.getFullYear(), this.pickedDate.value.getMonth(),
        this.pickedDate.value.getDate() + reminder.dayCount, reminder.timeCount, 0, 0, 0)
    }

    this.reminder=data.reminder;
    this.event={
      "purpose":"reminder",
      "value":this.reminder
    }
  
    this.eventCarrier.emit(this.event);
    //console.log(data)
    
    
  }
  reminderAddPicked(){
    
    let data={

      "reminder": new Date(this.pickedDate.value.getFullYear(), this.pickedDate.value.getMonth(),
      this.pickedDate.value.getDate() + this.timeSelected.dayCount, this.timeSelected.timeCount, 0, 0, 0)
    }
    //console.log(data)
    this.userService.addUpdateReminder(data).subscribe((data:any)=>{
      //console.log(data);
      this.dataService.changeMessage("Note Edited")
    });
  
  }
  
 
  
}