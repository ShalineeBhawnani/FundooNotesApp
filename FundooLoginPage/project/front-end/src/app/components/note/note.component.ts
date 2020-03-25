import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators}from '@angular/forms';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import { SharedService } from '../../services/shared.service';
import {MatSnackBar} from '@angular/material/snack-bar';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-note',
  templateUrl: './note.component.html',
  styleUrls: ['./note.component.scss'],
  providers:[AuthenticationService,UserService]
})
export class NoteComponent implements OnInit {

  title = new FormControl('', [
    Validators.required,

  ]);
  note = new FormControl('', [
    Validators.required,

  ]);
  save: Boolean
  message:string;
  noteLabels=[];
  labelIdList=[];
  color:string ="#ffffff";
  notes:string = ""; 
  is_archived:boolean=false;


  constructor(
    private userService: UserService,
    private snackBar:MatSnackBar,
    private dataService:DataService,
    private sharedService: SharedService) {

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
     is_archived:this.is_archived,  

  }
 
  this.userService.createNote(noteData).subscribe(
    (data) => {
      this.snackBar.open(data.toString(),'',{
        duration:3000,
        verticalPosition:'bottom'
      });
      console.log("data ",data)
    },
    error => {
      alert('Note Creation failed')
    
    });
    }
    

    recieveMessageFromIcon($event){
    if($event.purpose=="color"){
    {
      
      this.color=$event.value;
      console.log("my color",this.color)

    }
  }
  if($event.purpose=="archive"){
    console.log("archiving");
    this.is_archived=true;
    this.saveNotes();
    

  }


  }
}

