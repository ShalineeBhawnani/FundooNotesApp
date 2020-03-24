import { Component,Output,EventEmitter, OnInit } from '@angular/core';
import {FormBuilder, FormControl, FormGroup, Validators}from '@angular/forms';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-note',
  templateUrl: './note.component.html',
  styleUrls: ['./note.component.scss'],
  providers:[AuthenticationService,UserService]
})
export class NoteComponent implements OnInit {

  title = new FormControl('', [

  ]);
  note = new FormControl('', [

  ]);
  save: Boolean
  message:string;
  noteLabels=[];
  labelIdList=[];
  color:string ="#ffffff";
  notes:string = "";
  constructor(
    private userService: UserService,
    private alertService: AlertService,
    private dataService:DataService

  ) {

   }

   ngOnInit() {
  
    this.dataService.currentMessage.subscribe(message => this.message = message)
    }
    newMessage() {
      this.dataService.changeMessage("Note added")
    }

  saveNotes()

  {
    // this.messageEvent.emit(this.message);
    
    console.log(this.title.value);
     let noteData = {
     title : this.title.value,
     note : this.note.value,
     color:this.color,

  }
    this.userService.note(noteData)

  .subscribe(
      (data) => {
          console.log('Name: ' + this.title.value);
          this.newMessage();
          this.alertService.success('notes created successfully', true);
          // this.router.navigate(['/label']);
      },
      error => {
          this.alertService.error(error);

      });
    }

    recieveMessageFromIcon($event){
    if($event.purpose=="color"){
    {
      
      this.color=$event.value;
      console.log("my color",this.color)

    }
  }


  }
}