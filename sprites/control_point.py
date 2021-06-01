import pygame


class ControlPoint(pygame.sprite.Sprite):
    def __init__(self, x, y, color, cp_index, p_index):
        super(ControlPoint, self).__init__()
        self.cp_index = cp_index
        self.p_index = p_index
        self.original_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.original_image, color, (25, 25), 20)
        self.selected_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.selected_image, color, (25, 25), 25)
        pygame.draw.circle(self.selected_image,
                           (255, 255, 255), (25, 25), 25, 4)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.selected = False

    def get_event(self, event):
        pass

    def update(self, keys, control_points):
        mouse_pos = pygame.mouse.get_pos()
        mouse_buttons = pygame.mouse.get_pressed()
        self.selected = self.rect.collidepoint(
            mouse_pos) and any(mouse_buttons)
        self.image = self.selected_image if self.selected else self.original_image

        if self.selected:
            self.rect = self.image.get_rect(
                center=(mouse_pos[0], mouse_pos[1]))
            control_points[self.cp_index].points[self.p_index].x = mouse_pos[0]
            control_points[self.cp_index].points[self.p_index].y = mouse_pos[1]

        # return control_points

    def get_surf(self):
        return self.image

    def move_control_handler(self, control_points, x, y):

        deltaX = control_points[self.cp_index].points[self.p_index].x - x
        deltaY = control_points[self.cp_index].points[self.p_index].y - y

        control_points[self.cp_index].points[self.p_index].x = x
        control_points[self.cp_index].points[self.p_index].y = y

        # if is Path point
        if self.p_index == 0 or self.p_index == 3:
            related = self.get_related_path_point(self.cp_index, self.p_index, len(control_points) - 1)
            control_points[related[0]].points[related[1]].x = x
            control_points[related[0]].points[related[1]].y = y

            control_points = get_control_points(self.cp_index, self.p_index)



        #         //Get the related Control points and move them with the same delta.
        #         ControlPointHandlerId[] relatedControlPoints = bezierPathPointSelector.FindControlPointsOfPathPoint(controlPointHandlerId);
        #         controlPointQuartetCollection.GetBezierControlPoint(relatedControlPoints[0]).X -= deltaX;
        #         controlPointQuartetCollection.GetBezierControlPoint(relatedControlPoints[0]).Y -= deltaY;

        #         controlPointQuartetCollection.GetBezierControlPoint(relatedControlPoints[1]).X -= deltaX;
        #         controlPointQuartetCollection.GetBezierControlPoint(relatedControlPoints[1]).Y -= deltaY;
        #     }
        #     else // It is a control point
        #     {
        #         ControlPointHandlerId relatedControlPoint = bezierPathPointSelector.FindRelatedControlPoint(controlPointHandlerId);
        #         ControlPointHandlerId relatedPathPoint = bezierPathPointSelector.FindPathPointOfControlPoint(controlPointHandlerId);

        #         //The distance between the given control point and the path point must be the same as
        #         int xDistance = controlPointQuartetCollection.GetBezierControlPoint(relatedPathPoint).X - xPosition;
        #         int yDistance = controlPointQuartetCollection.GetBezierControlPoint(relatedPathPoint).Y - yPosition;

        #         controlPointQuartetCollection.GetBezierControlPoint(relatedControlPoint).X = controlPointQuartetCollection.GetBezierControlPoint(relatedPathPoint).X + xDistance;
        #         controlPointQuartetCollection.GetBezierControlPoint(relatedControlPoint).Y = controlPointQuartetCollection.GetBezierControlPoint(relatedPathPoint).Y + yDistance;
        #     }

        #     // The basic tricks in getting this to be a smooth curve across the whole path is to:
        #     // p3 of the each segment is in common to p0 of next each segment.
        #     // To make the circular, p3 of last segment must be same as p0 of 1st segment.
        #     // p2 and p3 of each segment must be on a strait line with p0 and p1 or the next segment. So this means

        #     // If left handler moved,  must also move corresponding path point so it intersects line to other handler at mid point
        #     // If right handler moved, must also move corresponding path point so it intersects line to other handler at mid point
        # }

        # public void AlignAll()
        # {
        #     for (int quartetIndex = 0; quartetIndex < controlPointQuartetCollection.NumberOfQuartets; quartetIndex++)
        #     {
        #         BezierControlPointQuartet quartet = controlPointQuartetCollection.GetQuartet(quartetIndex);
        #         for (int pointIndex = 0; pointIndex < 4; pointIndex++)
        #         {
        #             MoveControlHandlerTo(
        #                 new ControlPointHandlerId { ControlPointIndex = pointIndex, QuartetIndex = quartetIndex },
        #                 quartet.GetBezierControlPoint(pointIndex).X,
        #                 quartet.GetBezierControlPoint(pointIndex).Y);
        #         }
        #     }
        # }

        def get_related_path_point(self, cp_index, p_index, last_cp_index):
            related_p_index = 0
            related_cp_index = 0
            if p_index == 1:
                related_p_index = 2
                if cp_index == 0:
                    related_cp_index = last_cp_index
                elif cp_index > 0:
                    related_cp_index = cp_index - 1
            elif p_index == 2:
                related_p_index = 1
                if cp_index < last_cp_index:
                    related_cp_index = cp_index + 1
                else:
                    related_cp_index = 0

            return (related_cp_index, related_p_index)


        # public ControlPointHandlerId[] FindControlPointsOfPathPoint(ControlPointHandlerId pathPoint)
        # {
        #     var relatedControlPoints = new ControlPointHandlerId[2];

        #     if (pathPoint.ControlPointIndex == 0 )
        #     {
        #         relatedControlPoints[0] = new ControlPointHandlerId { ControlPointIndex = 1, QuartetIndex = pathPoint.QuartetIndex };

        #         if (pathPoint.QuartetIndex == 0)
        #         {
        #             relatedControlPoints[1] = new ControlPointHandlerId { ControlPointIndex = 2, QuartetIndex = GetLastQuartetIndex() };
        #         }
        #         else
        #         {
        #             relatedControlPoints[1] = new ControlPointHandlerId { ControlPointIndex = 2, QuartetIndex = pathPoint.QuartetIndex - 1 };
        #         }
        #     }
        #     else if (pathPoint.ControlPointIndex == 3)
        #     {
        #         relatedControlPoints[0] = new ControlPointHandlerId { ControlPointIndex = 2, QuartetIndex = pathPoint.QuartetIndex };

        #         if (pathPoint.QuartetIndex == 0 && controlPointQuartetCollection.NumberOfQuartets > 1)
        #         {
        #             relatedControlPoints[1] = new ControlPointHandlerId { ControlPointIndex = 1, QuartetIndex = pathPoint.QuartetIndex + 1 };
        #         }
        #         else
        #         {
        #             if (pathPoint.QuartetIndex == controlPointQuartetCollection.NumberOfQuartets - 1)
        #             {
        #                 relatedControlPoints[1] = new ControlPointHandlerId { ControlPointIndex = 1, QuartetIndex = 0 };
        #             }
        #             else
        #             {
        #                 relatedControlPoints[1] = new ControlPointHandlerId { ControlPointIndex = 1, QuartetIndex = pathPoint.QuartetIndex + 1 };
        #             }
        #         }
        #     }
            
        #     return relatedControlPoints;
        # }


