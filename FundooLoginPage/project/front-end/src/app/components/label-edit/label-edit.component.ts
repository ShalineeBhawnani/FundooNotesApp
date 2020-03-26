import { Component, OnInit,Inject,Output,EventEmitter} from '@angular/core';
import { MAT_DIALOG_DATA, throwMatDuplicatedDrawerError } from '@angular/material';
import { FormControl } from '@angular/forms';
import { UserService } from '../../services/user.service';
import { DataService } from '../../services/data.service';
import {Events} from '../../models/eventModel'

@Component({
  selector: 'app-label-edit',
  templateUrl: './label-edit.component.html',
  styleUrls: ['./label-edit.component.scss']
})
export class LabelEditComponent implements OnInit {
  label=new FormControl();
  editingLabel:string;
  event:Events;
  constructor(@Inject(MAT_DIALOG_DATA) private data: any,private userService:UserService,private dataService:DataService) { }
  @Output() eventCarrier = new EventEmitter<Events>();
  ngOnInit() {
  }
 isBeingEdited(label){
    this.editingLabel=label.id;
  }
  isEditVisible(label){
    if(this.editingLabel==label.id)
    return true;
    else
    return false;
  }
updateLabel(){
  let data={
    "label":this.label.value,
    "userId":localStorage.getItem('userId'),
    "isDeleted":false ,
    "id":this.editingLabel
  }
  this.userService.updateLabel(data).subscribe((data:any)=>{
    
    this.event={
      "purpose":"labelRefresh"
    }
    this.eventCarrier.emit(this.event)


  })
  console.log("fsdfsdfsd",this.label);
}
deleteLabel(){
  let data={
  
    "userId":localStorage.getItem('userId'),
    "isDeleted":true ,
    "id":this.editingLabel
  }
  this.userService.deleteLabel(data).subscribe((data:any)=>{
    
    this.event={
      "purpose":"labelRefresh"
    }
    

  }
  ) 
}


}