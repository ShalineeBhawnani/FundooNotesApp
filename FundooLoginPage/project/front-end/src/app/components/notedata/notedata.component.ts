import { Component, OnInit } from '@angular/core';
import {MAT_DIALOG_DATA, MatDialogRef} from "@angular/material";
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import { Message } from '@angular/compiler/src/i18n/i18n_ast';

@Component({
  selector: 'app-notedata',
  templateUrl: './notedata.component.html',
  styleUrls: ['./notedata.component.scss']
})
export class NotedataComponent implements OnInit {
 
  notes = [
    {   title: ' ',
        note: ' '}
      ]
      
  ParentData
 

  constructor(private userSerive: UserService) {
    this.getNotes();
   }
 
  ngOnInit() {

   
  }
  getNotes=()=>{

   

    this.userSerive.getAllNote().subscribe(
      data => {
        console.log(data)
        this.notes = data;
        this.ParentData = this.notes
      },
      
      error => {
        console.log(error);
      }
    );
  }

}
// getNotes(){

//   console.log(this.title.value);
//   let noteData = {
//   title : this.title.value,
//   note : this.note.value
 
// }
//  this.userService.getAllNote(noteData)

// .subscribe(
//    (data) => {
//        console.log('Name: ' + this.title.value);
//        this.alertService.success('notes got', true);
//        // this.router.navigate(['/label']);
//    },
//    error => {
//        this.alertService.error(error);

//    });
// }

// }

