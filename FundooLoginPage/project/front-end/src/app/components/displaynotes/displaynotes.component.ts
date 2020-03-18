import { Component, OnInit } from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
@Component({
  selector: 'app-displaynotes',
  templateUrl: './displaynotes.component.html',
  styleUrls: ['./displaynotes.component.scss']
})
export class DisplaynotesComponent implements OnInit {

  notes = [
    {   title: ' ',
        note: ' '}
      ]


  constructor(private userSerive: UserService) {

    this.getNotes();

   }
   getNotes=()=>{

      this.userSerive.getAllNote().subscribe(
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
