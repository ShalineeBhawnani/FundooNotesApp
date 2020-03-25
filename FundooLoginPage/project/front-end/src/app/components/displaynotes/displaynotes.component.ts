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
    this.dataService.currentMessage.subscribe(message => this.message = message)
    
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
  
    // displayNotes(){
    //   this.event={
    //     "purpose":"refresh",
    //   }
    
    
    //   this.eventCarrier.emit(this.event)
    //  }
    
    openDialog(note) {
      {
      this.fileNameDialogRef = this.dialog.open(NoteDialogComponent, {
      hasBackdrop: false,
      data: note
      });
      }
      }


}




