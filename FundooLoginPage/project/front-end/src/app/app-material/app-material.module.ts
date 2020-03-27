import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FlexLayoutModule } from '@angular/flex-layout';
import { MatIconModule } from '@angular/material/icon';
import { MatCardModule } from '@angular/material/card';
import { MatListModule } from '@angular/material/list';
import { MatSortModule } from '@angular/material/sort';
import { MatInputModule } from '@angular/material/input';
import { MatTableModule } from '@angular/material/table';
import { MatButtonModule } from '@angular/material/button';
import { MatDialogModule } from '@angular/material/dialog';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatFormFieldModule } from '@angular/material/form-field';
import {MatCheckboxModule} from '@angular/material/checkbox';
import {MatExpansionModule,MatDatepickerModule} from '@angular/material';
import {MatSnackBarModule} from '@angular/material/snack-bar';
import {MatButtonToggleModule} from '@angular/material/button-toggle';
import {MatSelectModule} from '@angular/material/select';
import {MatNativeDateModule,MatRadioModule, MatTabsModule, MatTooltipModule,} from  '@angular/material';



@NgModule({
    imports: [
        CommonModule,
        MatIconModule,
        MatCardModule,
        MatListModule,
        MatSortModule,
        MatInputModule,
        MatTableModule,
        MatButtonModule,
        MatDialogModule,
        MatSidenavModule,
        MatToolbarModule,
        FlexLayoutModule,
        MatFormFieldModule,
        MatCheckboxModule,
        MatExpansionModule,
        MatSnackBarModule,
        MatButtonToggleModule,
        MatDatepickerModule,
        MatSelectModule,
        MatNativeDateModule,
        MatRadioModule,
        MatTabsModule,
        MatTooltipModule



    ],
    exports: [
        MatIconModule,
        MatCardModule,
        MatListModule,
        MatSortModule,
        MatInputModule,
        MatTableModule,
        MatButtonModule,
        MatDialogModule,
        MatSidenavModule,
        MatToolbarModule,
        FlexLayoutModule,
        MatFormFieldModule,
        MatCheckboxModule,
        MatExpansionModule,
        MatSnackBarModule,
        MatButtonToggleModule,
        MatDialogModule,
        MatDatepickerModule,  
        MatSelectModule,
        MatNativeDateModule,
        MatRadioModule,
        MatTabsModule,
        MatTooltipModule,



    ],
    declarations: []
})
export class AppMaterialModule { }
