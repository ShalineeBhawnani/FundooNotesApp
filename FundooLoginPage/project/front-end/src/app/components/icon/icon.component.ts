import { Component, OnInit,EventEmitter,Output } from '@angular/core';
import {Events} from '../../models/eventModel';
import {DataService} from '../../services/data.service';
import { UserService } from '../../services/user.service';
import {Labels} from '../../models/labels';
import { FormControl } from '@angular/forms';
import { MatDialog } from '@angular/material';
import { CollaboratorComponent } from '../collaborator/collaborator.component';

@Component({
  selector: 'app-icon',
  templateUrl: './icon.component.html',
  styleUrls: ['./icon.component.scss']
})
export class IconComponent implements OnInit {
  event:Events;
  labelIdList:string[];
  colors=[
  "#e8eaed","#e6c9a8","#fdcfe8","#d7aefb","#f28b82","#fbbc04","#fff475","#ccff90","#a7ffeb",
    "#cbf0f8","#aecbfa","#d7aefb"
  ]
  newLabel:string;
  labels:Labels[];
  save:Boolean=false;
  message:string;
  note:any;
  reminder:any;
  
  labelCheck = new FormControl();
  dummy:boolean=false;
  @Output() eventCarrier = new EventEmitter<Events>();
  @Output() saveNotes = new EventEmitter<Boolean>();

  constructor(private dataService:DataService,private userService:UserService,private dialog:MatDialog) { }

  ngOnInit() {
    this.dataService.currentMessage.subscribe(message => this.message = message)
    this.getLabels();
    
  }
  
  saveNote() {
    this.save=true;
    this.saveNotes.emit(this.save);
  }
  archive(){
    this.event={
      "purpose":"archive",
    }
   
    this.eventCarrier.emit(this.event);
  }
  deleteNotes(){
    this.event={
      "purpose":"deleteNote",
    }
    this.eventCarrier.emit(this.event);
  }

  addCollaborator(){
    let dialogref = this.dialog.open(CollaboratorComponent,{
      data : {
        note:this.note     
      }
    });
    dialogref.afterClosed().subscribe(result=> {
      console.log("dialog result ", result);
    })
  }
  addLabel(){
   
    let data={
      "label":this.newLabel,
      "isDeleted":false 
    }
    console.log("label add again",data)
    console.log("created label",data)
    this.userService.label(data).subscribe((data:any)=>{
      this.getLabels();
      this.newLabel="";
 

    })
  }
   
  getLabels(){
    console.log("getting labels",this.labels)
    this.userService.getAllLabel().subscribe(
      data => {
        this.labels = data;
        console.log("my data label",data)
      },
      
      error => {
        console.log(error);
      }
    );
  }
  
  labelAddOrRemove(label){
    let data={
      "label":label.id
    }
    console.log("checklist labelAddOrRemove",data)
    
    this.event={
      "purpose":"addLabel",
      "value":data
    }
   
    this.eventCarrier.emit(this.event);
  }

  colorElement(color){
    console.log("color",color)
    this.event={
      "purpose":"color",
      "value":color
    }
    console.log(this.note)
    this.eventCarrier.emit(this.event);

  }
  fileInput(){
    console.log("clicked")
    this.event={
      "purpose":"add_picture",
    }
   
    this.eventCarrier.emit(this.event);
  }
  addReminder(){
    let data={
      "noteIdList":[this.note['id']],
      "reminder":this.reminder
    }
    this.event={
      "purpose":"reminder",
      "value":data
    }

    this.eventCarrier.emit(this.event);

  }
  recieveMessageFromReminder($event){
    
      this.eventCarrier.emit($event)
    
  }
  
}
