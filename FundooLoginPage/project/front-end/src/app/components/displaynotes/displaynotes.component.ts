import { Component,Input, OnInit ,OnDestroy} from '@angular/core';
import { AlertService } from '../../services/alert.service';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';
import {MatDialog, MatDialogRef,MAT_DIALOG_DATA,MatDialogConfig} from '@angular/material/dialog';
import { NoteDialogComponent } from '../note-dialog/note-dialog.component';
import { HostListener } from "@angular/core";
import { MyNavComponent } from '../my-nav/my-nav.component';
export interface DialogData {
  
  }
@Component({

  selector: 'app-displaynotes',
  templateUrl: './displaynotes.component.html',
  styleUrls: ['./displaynotes.component.scss'],
  providers: [UserService]
})

export class DisplaynotesComponent implements OnInit,OnDestroy {
  screenWidth:number=1300;
  screenHeight:number;
  message:string;
  displayValue:string="flex";
  widthCard:string="250px";
  @Input() sendDataToChild=[];

fileNameDialogRef: MatDialogRef<NoteDialogComponent>;

  notes =[]
  labels=[]
  data = {
    viewLayoutType: "row wrap",
    viewStyling: true
  }

  constructor(private userSerive: UserService,public dialog:MatDialog,
    private dataService: DataService,private nav: MyNavComponent,) {

   }

  ngOnInit(){

    this.dataService.currentMessage.subscribe(message => {
      if(message=='grid View')
      { 
        this.setView();
      
      }
    })
     
    

  }
  @HostListener('window:resize', ['$event'])
  onResize(event?) {

     this.screenHeight = window.innerHeight;
     this.screenWidth = window.innerWidth;
     this.setView();
  }
  setView(){
    if(this.displayValue=="flex")
    {
      this.displayValue="table-cell";
      this.widthCard=this.screenWidth/2.4+"px";
  }
    else
    {
    this.displayValue="flex";
      this.widthCard="250px"
  }

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
