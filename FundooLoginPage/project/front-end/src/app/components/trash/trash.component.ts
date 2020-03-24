import { Component, OnInit } from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
@Component({
  selector: 'app-trash',
  templateUrl: './trash.component.html',
  styleUrls: ['./trash.component.scss']
})
export class TrashComponent implements OnInit {
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

      this.userSerive.bin().subscribe(
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
