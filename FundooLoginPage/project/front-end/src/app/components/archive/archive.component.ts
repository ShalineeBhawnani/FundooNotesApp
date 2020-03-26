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
      ParentData

  constructor(private userSerive: UserService) {

  }

    ngOnInit(){

      this.getNotes();

    }
   
   getNotes=()=>{

      this.userSerive.ArchiveNote().subscribe(
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
