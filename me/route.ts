// me/route.ts
import { Router } from 'express';
import { getMe } from './controller';
import { authenticate } from '../middleware/auth'; // or wherever your auth lives

const router = Router();

router.get('/me', authenticate, getMe);

export default router;