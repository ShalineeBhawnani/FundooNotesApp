import { BreakpointObserver, Breakpoints, BreakpointState } from '@angular/cdk/layout';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import {ChangeDetectorRef, Component, OnDestroy} from '@angular/core';
import {MediaMatcher} from '@angular/cdk/layout';
import {Router} from '@angular/router'
import {Labels} from '../../models/labels';
import {LabelEditComponent} from '../label-edit/label-edit.component';
import {MatDialog} from '@angular/material/dialog';
import { DataService } from '../../services/data.service';


@Component({
  selector: 'app-my-nav',
  templateUrl: './my-nav.component.html',
  styleUrls: ['./my-nav.component.scss']
})
export class MyNavComponent implements OnDestroy{
  labels:Labels[];

  mobileQuery: MediaQueryList;

  private _mobileQueryListener: () => void;

  constructor(changeDetectorRef: ChangeDetectorRef, media: MediaMatcher,private routing:Router,private dataService:DataService, private dialog:MatDialog) {
    this.mobileQuery = media.matchMedia('(max-width: 600px)');
    this._mobileQueryListener = () => changeDetectorRef.detectChanges();
    this.mobileQuery.addListener(this._mobileQueryListener);
  }

  // navigateTrash(){ 
  //   console.log("navigating to trash")
  //   this.routing.navigate(['nav/bin']);
  // }
  // navigateArchive(){
  //   this.routing.navigate(['nav/archive']);
  // }

  navigateToLabel(label){
  console.log(label);
    
    this.dataService.labelNext(label)
    this.routing.navigate(['/nav/label'+label])
  }
  openLabelEditBox(){
    console.log("inside dash open label func")
    let dialogref = this.dialog.open(LabelEditComponent,
      {
        
        data : {
          label:this.labels  
                
        }
        
      });
    
    dialogref.afterClosed().subscribe(result=> {
      //console.log("dialog result ", result);
      
    })
  }
  
  ngOnDestroy(): void {
    this.mobileQuery.removeListener(this._mobileQueryListener);
  }
  
}
