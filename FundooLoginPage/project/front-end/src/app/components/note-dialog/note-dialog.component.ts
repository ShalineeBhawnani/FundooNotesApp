import { Component, OnInit ,Inject} from '@angular/core';
import { MatDialogRef,MAT_DIALOG_DATA} from '@angular/material/dialog';
import { UserService } from '../../services/user.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import { DataService } from '../../services/data.service';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-note-dialog',
  templateUrl: './note-dialog.component.html',
  styleUrls: ['./note-dialog.component.scss']
})
export class NoteDialogComponent implements OnInit {

  title = new FormControl();
  note = new FormControl();
  save: Boolean
  message:string;
  label_note=[];
  color:string ="#ffffff";
  notes:string = ""; 
  id:string;
  is_archived:boolean=false;
  is_bin:boolean=false;
  collaborators=[];
  add_picture: [null]
  noteFinal:string;
  titleFinal:string;
  notedata:any;

constructor( private dialogRef: MatDialogRef<NoteDialogComponent>,
  @Inject(MAT_DIALOG_DATA) public data: any,
  private userService: UserService,
  private snackBar:MatSnackBar,
  private dataService:DataService) {
  console.log("this data: ", this.data);
  }
 
  ngOnInit() {

  }
  updateNote() {
    this.noteFinal=this.note.value;
    this.titleFinal=this.title.value;

    
    if(this.note.value==null){
      this.noteFinal=this.data.note;
    }

    if(this.title.value==null){
      this.titleFinal=this.data.title;
    }
 

    this.notedata = {
      title: this.titleFinal,
      note: this.noteFinal,
      is_archived:this.is_archived,
      color:this.color,
    }
    if((this.notedata.title == null) && (this.data.title != null))
    {
      this.notedata.title = this.data.title;
    }
    if((this.notedata.note == null) && (this.data.note != null))
    {
      this.notedata.note = this.data.note;
    }

    if((this.notedata.title == "") && (this.notedata.note == ""))
    {
      this.notedata.title = "both are empty";
      this.notedata.note = "both are empty";
    
    }
    this.dialogRef.close();
 
    this.userService.updateNotes(this.notedata,this.data.id)
    .subscribe(
        (data) => {
          this.snackBar.open(data.toString(),'',{
            duration:3000,
            verticalPosition:'bottom'
          });
            
        },
        error => {
          alert('Note updation failed')

        });
        this.dialogRef.close(this.notedata);
  }


    recieveMessageFromIcon($event)
    {
    
      if($event.purpose=="color"){
        console.log("color func nside")
        this.data.color=$event.value;
        {
      
          this.notedata = {
            title: this.titleFinal,
            note: this.noteFinal,
            is_archived:true,
            color:$event.value,
            
          }
            
          
         this.userService.updateNotes(this.notedata,this.data.id)
         .subscribe(
         (data) => {
           this.snackBar.open(data.toString(),'',{
             duration:3000,
             verticalPosition:'bottom'
           });
             
         },
         error => {
           alert('Note updation failed')
  
         });
        }
      }
      if($event.purpose=="archive"){
        this.is_archived=true;

        this.notedata = {
          title: this.titleFinal,
          note: this.noteFinal,
          is_archived:true,
          
        }
          
        
       this.userService.updateNotes(this.notedata,this.data.id)
       .subscribe(
       (data) => {
         this.snackBar.open(data.toString(),'',{
           duration:3000,
           verticalPosition:'bottom'
         });
           
       },
       error => {
         alert('Note updation failed')

       });
        
       
     }
   }
     
      }
    


