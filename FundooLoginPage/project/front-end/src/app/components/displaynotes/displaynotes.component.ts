import { Component,Input, OnInit ,OnDestroy} from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';
import {MatDialog, MatDialogRef,MAT_DIALOG_DATA,MatDialogConfig} from '@angular/material/dialog';
import { NoteDialogComponent } from '../note-dialog/note-dialog.component';

export interface DialogData {
  
  }
@Component({

  selector: 'app-displaynotes',
  templateUrl: './displaynotes.component.html',
  styleUrls: ['./displaynotes.component.scss'],
  providers: [UserService]
})

export class DisplaynotesComponent implements OnInit,OnDestroy {
  // note$: any;
  // subscription: Subscription;
  message:string;
  @Input() sendDataToChild=[];

fileNameDialogRef: MatDialogRef<NoteDialogComponent>;

  notes =[]
 

  constructor(private userSerive: UserService,public dialog:MatDialog,
    private dataService: DataService) {

   }

  ngOnInit(){

    console.log("data",this.sendDataToChild)
    // this.dataService.currentMessage.subscribe(message => this.message = message)
    
  }

  ngAfterContentInit() {

    try {
    
    setTimeout(() => {
    
    this.notes = this.sendDataToChild;
    console.log("data send",this.notes)
    
    
    }, 2000);
    
    } catch (error) {
    
    console.log('error in ngAfterContentInit in display component');
    }
    }
  ngOnDestroy() {
 
    }
  
  
    openDialog(note) {
      {
      this.fileNameDialogRef = this.dialog.open(NoteDialogComponent, {
      hasBackdrop: false,
      data: note
       
    });

    this.fileNameDialogRef.afterClosed().subscribe(
      data => console.log("Dialog output:", data)
  );    
  
  }
}

}



// import { Component, OnInit,Inject, OnDestroy, Input, AfterContentInit } from '@angular/core';
// import { UserService } from '../user.service';
// import {MatDialog, MatDialogRef,MAT_DIALOG_DATA,MatDialogConfig} from '@angular/material/dialog';
// import { DialogueBoxComponent } from '../dialogue-box/dialogue-box.component';

// export interface DialogData {
//   title: string;
//   takeNote: string;
 
// }

// @Component({
//   selector: 'app-displaynote',
//   templateUrl: './displaynote.component.html',
//   styleUrls: ['./displaynote.component.css'],
//   providers: [UserService]
// })
// export class DisplaynoteComponent implements OnInit,AfterContentInit{

//   @Input() sendDataToChild=[];

//   DialogRef: MatDialogRef<DialogueBoxComponent>;
//   usernotes=[]

  

// constructor(  private userService: UserService,
//               public dialog:MatDialog,)
//            {}

// ngOnInit()
// {
//  console.log("data",this.sendDataToChild)
// }
// ngAfterContentInit()
// {
//   try{
//     setTimeout(() =>{
//       this.usernotes = this.sendDataToChild;
//       console.log("data send",this.usernotes)
//     },2000);
//   }catch(error){
//     console.log('error in ng after content init');
//   }
// }




// openDialog(note) {
//   {
//     this.DialogRef = this.dialog.open(DialogueBoxComponent, {
//       hasBackdrop: false,
//       data: note
      
//     });

//     this.DialogRef.afterClosed().subscribe(
//       data => console.log("Dialog output:", data)
//   );    
  
//   }
// }

// }