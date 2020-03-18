import { Component, OnInit } from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';

@Component({
  selector: 'app-archive',
  templateUrl: './archive.component.html',
  styleUrls: ['./archive.component.scss']
})
export class ArchiveComponent implements OnInit {

  notes = [
    {   title: ' ',
        note: ' '}
      ]


  constructor(private userSerive: UserService) {

    this.getNotes();

   }
   getNotes=()=>{

      this.userSerive.ArchiveNote().subscribe(
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
