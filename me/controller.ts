// me/controller.ts
import { Request, Response } from 'express';

export const getMe = (req: Request, res: Response) => {
  const user = req.user; // Assuming you've attached user via auth middleware
  if (!user) return res.status(401).json({ message: 'Unauthorized' });

  res.status(200).json({ user });
};