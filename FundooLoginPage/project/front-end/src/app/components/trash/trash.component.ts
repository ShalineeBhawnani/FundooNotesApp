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


  constructor(private userSerive: UserService) {

    this.getNotes();

   }
   getNotes=()=>{

      this.userSerive.Trash().subscribe(
        data => {
          this.notes = data;
        },
        error => {
          console.log(error);
        }
      );
    }


  ngOnInit(){

  }


}

