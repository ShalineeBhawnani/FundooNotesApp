import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators}from '@angular/forms';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import { MatSnackBar } from '@angular/material/snack-bar';
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
  label_note=[];
  color:string ="#ffffff";
  notes:string = ""; 
  id:string;
  is_archived:boolean=false;
  is_bin:boolean=false;
  collaborators=[];
  reminder:string;
  add_picture: [null]
  ImageUrl:any;
  fileToUpload: any;
  profileImageUrl:any;
  
  constructor(
    private userService: UserService,
    private snackBar:MatSnackBar,
    private dataService:DataService,
    ) {

   }

   ngOnInit() {
  
    this.dataService.currentMessage.subscribe(message => this.message = message)
    console.log(this.message)


   
    
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
     reminder:this.reminder,
     is_archived:this.is_archived, 
     is_bin:this.is_bin,
     label_note:this.label_note,
     collaborators:this.collaborators,
     add_picture:this.add_picture,
     
  }
  

  console.log("note label",noteData.label_note)
  this.userService.createNote(noteData).subscribe(
    (data) => {
      this.newMessage();
      this.snackBar.open(data.toString(),'',{
        duration:3000,
        verticalPosition:'bottom'
      });
      console.log("data creation ",data.toString())
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
  if($event.purpose=="deleteNote"){
    console.log("deleteNote");
    this.is_bin=true;
    this.saveNotes();
    

  }
  
  if($event.purpose=="addLabel"){
   
    console.log("addLabel",this.label_note.push($event.value.label));
    this.label_note.push($event.value.label)
  
         }
    
  if($event.purpose=="add_picture"){
   
    console.log("file upload");
    
  }
  
  
}


  }


