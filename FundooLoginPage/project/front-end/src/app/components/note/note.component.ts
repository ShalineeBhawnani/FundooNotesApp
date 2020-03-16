import { Component, OnInit } from '@angular/core';
import {FormBuilder, FormControl, FormGroup, Validators}from '@angular/forms';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';

@Component({
  selector: 'app-note',
  templateUrl: './note.component.html',
  styleUrls: ['./note.component.css'],
  providers:[AuthenticationService,UserService]
})
export class NoteComponent implements OnInit {
  title = new FormControl('', [

  ]);
  note = new FormControl('', [

  ]);


  constructor(
    private userService: UserService,
    private alertService: AlertService,

  ) {

   }

  ngOnInit() {

  }

  saveNotes()

  {
    console.log(this.title.value);
     let noteData = {
     title : this.title.value,
     note : this.note.value

  }
    this.userService.note(noteData)

  .subscribe(
      (data) => {
          console.log('Name: ' + this.title.value);
          this.alertService.success('notes created successfully', true);
          // this.router.navigate(['/label']);
      },
      error => {
          this.alertService.error(error);

      });
}

  }



