import { Component,Input, OnInit ,OnDestroy} from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { AuthenticationService } from '../../services/authentication.service';
import {MatDialog, MatDialogRef,MAT_DIALOG_DATA,MatDialogConfig} from '@angular/material/dialog';
import { NoteDialogComponent } from '../note-dialog/note-dialog.component';
import { SharedService } from '../../services/shared.service';
import { Subscription } from 'rxjs';

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
   
  @Input() sendDataToChild=[];

fileNameDialogRef: MatDialogRef<NoteDialogComponent>;

  // notes = [
  //   {   title: ' ',
  //       note: ' '}
  //     ]
  notes =[]

  constructor(private userSerive: UserService,public dialog:MatDialog,
    private sharedService: SharedService) {

    // this.getNotes();
    // this.note$ = this.sharedService.getMessage();

   }

  ngOnInit(){

    console.log("data",this.sendDataToChild)


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
    // unsubscribe to ensure no memory leaks
    // this.subscription.unsubscribe();
    }
  //  getNotes=()=>{

  //     this.userSerive.getAllNote().subscribe(
  //       data => {
  //         this.notes = data;
  //       },
  //       error => {
  //         console.log(error);
  //       }
  //     );
  //   }
    openDialog(note) {
      {
      this.fileNameDialogRef = this.dialog.open(NoteDialogComponent, {
      hasBackdrop: false,
      data: note
      });
      }
      }


}




