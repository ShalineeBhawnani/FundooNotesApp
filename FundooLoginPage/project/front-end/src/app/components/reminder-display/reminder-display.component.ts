import { Component, OnInit } from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';


@Component({
  selector: 'app-reminder-display',
  templateUrl: './reminder-display.component.html',
  styleUrls: ['./reminder-display.component.scss']
})
export class ReminderDisplayComponent implements OnInit {

  notes = [
    {   title: ' ',
        note: ' '}
      ]
      ParentData

  constructor(private userSerive: UserService) {

  }

    ngOnInit(){

      this.getNotes();

    }
   
   getNotes=()=>{

      this.userSerive.getReminder().subscribe(
        data => {
          console.log("my data",data)
          this.notes = data;
          this.ParentData = this.notes
        },
        error => {
          console.log(error);
        }
      );
    }

}
